from flask import Flask, render_template, request
import re

app = Flask(__name__)

def has_uppercase(string):
    for char in string:
        if char.isupper():
            return True
    return False

def has_lowercase(string):
    for char in string:
        if char.islower():
            return True
    return False

conditions=["Must have and uppercase letter somewhere", "Must have and lowercase letter somewhere", "Must end with a digit"]

@app.route("/")
def index():
    return render_template("ex_index.html", conditions=conditions)

@app.route("/report")
def report():
    username=request.args.get("username")
    passed=True
    checks=[]

    if has_uppercase(username):
        checks.append(conditions[0] + "-- Passed")
    else:
        checks.append(conditions[0] + "-- Failed")
        passed=False

    if has_lowercase(username):
        checks.append(conditions[1] + "-- Passed")
    else:
        checks.append(conditions[1] + "-- Failed")
        passed=False

    if username[-1].isdigit():
        checks.append(conditions[2] + "-- Passed")
    else:
        checks.append(conditions[2] + "-- Failed")
        passed=False

    
    return render_template("ex_report.html", username=username, passed=passed, checks=checks)

if __name__ == "__main__":
    app.run(debug=True)