from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    my_name = "Hitessssssssssssssssshhhh Kuuberrrrrrrrrrrrrrrrrrrrrrrrr"
    reasons = [
            "Saved the universe twice from intergalactic parasites.",
            "Engaged in philanthropy, providing potions to alien civilizations in need.",
            "Enhanced the energy of over 12,432,123 dimming stars, saving countless lives."
            ]
    return render_template("homepage.html", my_name = my_name, reasons = reasons)
          

if __name__ == "__main__":
    app.run(debug=True)