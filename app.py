from flask import Flask, request, render_template, redirect
import json
from setting import username, password
from helper import fetch_user
from requests.auth import HTTPBasicAuth
import requests


app = Flask(__name__)
authentication = HTTPBasicAuth(username, password)
target_user = 'damminhtien'


def return_template(template, data, error):
	if not error:
		return render_template(template, data=data)
	return error


@app.route('/')
def index():
	data = {}
	error = {}

	try:
	    data['user'] = fetch_user(target_user, authentication)
	except Exception as e:
		error['fetch_user'] = str(e)

	try:
		data['lang'] = fetch_lang(target_user, authentication)
	except Exception as e:
		error['fetch_lang'] = str(e)

	return return_template('index.html', data=data, error=error)


@app.route('/user/<user>')
def user(user):
	target_user = user
	data = {}
	error = {}

	try:
	    data['user'] = fetch_user(target_user, authentication)
	except Exception as e:
		error['fetch_user'] = str(e)

	try:
		data['lang'] = fetch_lang(target_user, authentication)
	except Exception as e:
		error['fetch_lang'] = str(e)

	return return_template('index.html', data=data, error=error)


if __name__ == '__main__':
	app.run(host='0.0.0.0', threaded=True, port=5000)