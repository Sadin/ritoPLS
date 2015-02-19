from flask import Flask
from flask import render_template
import requests, json, pprint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("template.html")


if __name__ == '__main__':
    app.run()
