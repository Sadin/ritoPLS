from flask import Flask, render_template, request, abort
import requests, json, pprint

# Logic
app = Flask(__name__, static_path='/static')

@app.route('/')
def index(default=''):
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
