from flask import Flask
from flask import render_template
import datetime

microweb_app = Flask(__name__)

@microweb_app.route("/")
def main():
    return render_template("index.html" , datetime_now = datetime.datetime.now())


@microweb_app.route("/map")
def showMap():
    return render_template("map.html")

if __name__ == "__main__":
    microweb_app.run(host="0.0.0.0", port=5050)
