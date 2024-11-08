from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<marquee><h1>Intergalactic super warrior Hitesh</h1></marquee>"

@app.route("/information")
def information():
    return """
<h1>
My Accomplishments:
<ul>
    <li>Saved the universe twice from intergalactic parasites.</li>
    <li>Engaged in philanthropy, providing potions to alien civilizations in need.</li>
    <li>Enhanced the energy of over 12,432,123 dimming stars, saving countless lives.</li>
</ul>
</h1>
"""

if __name__ == "__main__":
    app.run()