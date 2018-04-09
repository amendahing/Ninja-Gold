from flask import Flask, render_template, request, redirect, session
import random, time, datetime

app = Flask(__name__)
app.secret_key = "racecar"

@app.route('/')
def index():
    if "log" not in session:
        session["log"] = []

    if "gold" in session:
        session["gold"] += 0
    else:
        session["gold"] = 0
    return render_template("index.html", log=session["log"])


@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form["building"] == "farm":
        session["gold"] += random.randrange(10, 21)
        session["log"].append("Entered Farm and earned " + str(random.randrange(10, 21)) + " Gold" + " (" + time.ctime() + ")")


    elif request.form["building"] == "cave":
        session["gold"] += random.randrange(5, 11)
        session["log"].append("Entered Cave and earned " + str(random.randrange(10, 21)) + " Gold" + " (" + time.ctime() + ")")

    elif request.form["building"] == "house":
        session["gold"] += random.randrange(2, 6)
        session["log"].append("Entered House and earned " + str(random.randrange(10, 21)) + " Gold" +  " (" + time.ctime() + ")")

    elif request.form["building"] == "casino":
        session["gold"] += random.randrange(-50, 51)
        session["log"].append("Entered Casino and earned " + str(random.randrange(10, 21)) + " Gold" +  " (" + time.ctime() + ")")

    print session["log"]
    return redirect('/')


app.run(debug=True)
