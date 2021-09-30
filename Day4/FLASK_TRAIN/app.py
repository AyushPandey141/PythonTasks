# TASK:To Make 3 decorators
# Program By:Ayush Pandey
# Email Id:1805290@kiit.ac.in
# DATE:22-Sept-2021
# Python Version:3.7
# CAVEATS:None
# LICENSE:None

from flask import Flask, request
from flask import render_template
from flask import redirect
from flask import url_for
import json
import pymongo

client = pymongo.MongoClient()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/bye')
def exit():
    return render_template('exit.html')


def insert_data(dict1):
    data = json.load(open('Flask_Insert.json'))

    # convert data to list if not
    if type(data) is dict:
        data = [data]

    # append new item to data lit
    data.append(dict1)

    # write list to file
    with open('Flask_Insert.json', 'w') as outfile:
        json.dump(data, outfile)


@app.route('/predict', methods=["POST"])
def get():
    if request.method == 'POST':
        data1 = request.form['a']
        data2 = request.form['s']
        if(client):
            client['FLASK']['User'].insert({'name:': data1, 'email': data2})
            w = {'name': data1, 'email': data2}
            insert_data(w)
        return render_template('exit.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
