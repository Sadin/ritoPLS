from flask import Flask, render_template
from flask.ext.triangle import Triangle
import requests, json, pprint

app = Flask(__name__, static_path='/static')
Triangle(app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
