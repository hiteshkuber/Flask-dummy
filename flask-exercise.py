from flask import Flask

app = Flask(__name__)

@app.route("/")
def homePage():
    return "Hey this is Puppy latin execise."

@app.route("/puppy_latin/<name>")
def latinise(name):
    return f"Latinised name is {name}y" if name[-1] != 'y' else f"Latinised name is {name[0:-1:]}itiful"

if __name__ == "__main__":
    app.run(debug=True)
