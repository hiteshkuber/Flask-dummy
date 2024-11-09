from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/puppy/<name>")
def pup_name(name):
    return render_template("puppy.html", name=name)

@app.route("/puppy")
def try_url():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)

