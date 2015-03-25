from flask import Flask, render_template, request, redirect, url_for, abort
import requests, json, pprint
from riot import summoner

# Logic
app = Flask(__name__, static_path='/static')

# application wide definitions


@app.route('/')
def index():
    return render_template('index.html', landing=True)

@app.route('/summoner', methods=['GET', 'POST'])
def summoner():
    error = False
    bad_name = False
    if request.method == 'POST':
        user_name = request.form['name']
        payload = {'api_key': 'b0afea27-1602-4ed8-aff5-24caf6bbb2d1'}

        # attempt to query the riot games api for the summoner basic info
        s_info = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{}".format(user_name), params=payload) #format the API request URL
        if s_info.status_code == 200:
            print("SUCCESS! The summoner {} was found!".format(user_name))

            pprint.pprint(s_info.json())
            error = False
        else:
            print("ERROR The summoner {} was not found!".format(user_name))
            error = True

        return render_template('summoner.html', summoner=request.form['name'], failure=error)

if __name__ == '__main__':
    app.run(debug=True)
