from flask import Flask, render_template, request, redirect, url_for, abort
import requests, json, pprint

# Logic
app = Flask(__name__, static_path='/static')

@app.route('/')
def index():
    return render_template('index.html', landing=True)

@app.route('/summoner', methods=['GET', 'POST'])
def summoner():
	error = None
	if request.method == 'POST':
	    user_name = request.form['name']

	return render_template('summoner.html', summoner=user_name)


if __name__ == '__main__':
    app.run(debug=True)
