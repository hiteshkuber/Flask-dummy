from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    my_name = "Hitessssssssssssssssshhhh Kuuberrrrrrrrrrrrrrrrrrrrrrrrr"
    return render_template("homepage.html", my_name = my_name)
          

if __name__ == "__main__":
    app.run(debug=True)