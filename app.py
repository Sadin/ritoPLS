from flask import Flask, render_template, request, abort
from flask.ext.triangle import Triangle, Form
from flask.ext.triangle.widgets.standard import TextInput
import requests, json, pprint

# Logic

class Profile(Form):

    fname = TextInput('profile.fname', label='First Name', required=True)
    lname = TextInput('profile.lname', label='Last Name', required=True)
    bdate = TextInput('profile.bdate', label='Birthdate', required=True)
    bio = TextInput('profile.bio', label='Bio')



app = Flask(__name__, static_path='/static')
Triangle(app)

@app.route('/')
def index(default=''):
    return render_template('index.html', default=default)
@app.route('/query', methods=['GET', 'POST'])
def query():

    form = Profile(vroot='query')     # only the content of profile is
                                        # sent. We use a virtual root to
                                        # shift the schema.

    if request.method == 'POST':
        if form.validate(request.json): # validate the received data
            return 'ok !'
        else:
            abort(400)
    else:
        return render_template('query.html', form=form)



if __name__ == '__main__':
    app.run()
