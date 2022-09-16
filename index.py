from flask import Flask, render_template
import requests
import random

app = Flask(__name__)
res = None

def getBlogData():
    #https://mocki.io/fake-json-api --> json website
    end_point = "https://mocki.io/v1/f4aff8ed-6d04-43e1-ac4f-ce373a4a64e0"
    res = requests.get(end_point).json()
    return res

def randomNumberGenerator():
    global num
    num = random.randint(1,10)


@app.route("/")
def IndexFun():
    randomNumberGenerator()
    return render_template("index.html")


@app.route("/NumberGuessing/<int:value>")
def NumberGuessing_fun(value):
    return render_template("GuessingNumber.html", number = num,guessedVal = value)


@app.route("/Blog")
def blogIndexFun():
    global res
    res = getBlogData()
    return render_template("blogindex.html", jobj=res)


@app.route("/Detail_Blog/<int:num>")
def showDetailBlog(num):
    return render_template("blog.html",jobj=res,blogNum = num-1)


if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")
