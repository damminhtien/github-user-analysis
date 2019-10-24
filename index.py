from flask import Flask, request, render_template, redirect
import requests
import json
from setting import username, password
from requests.auth import HTTPBasicAuth


app = Flask(__name__)
authentication = HTTPBasicAuth(username, password)
target_user = 'damminhtien'


def fetch_user(target_user):
	user_data = requests.get('https://api.github.com/users/' + target_user, auth = authentication).json()
	data = {}
	data['login'] = user_data['login']
	data['name'] = user_data['name']
	data['avatar_url'] = user_data['avatar_url']
	data['company'] = user_data['company']
	data['bio'] = user_data['bio']
	data['public_repos'] = user_data['public_repos']
	data['followers'] = user_data['followers']
	data['following'] = user_data['following']
	data['created_at'] = user_data['created_at']

	return data


@app.route('/')
def index():
	data = {}
	error = {}

	try:
	    data['user'] = fetch_user(target_user)
	except Exception as e:
		error['fetch_user'] = str(e)

	return render_template('index.html', data=data)


app.run(use_debugger= True, debug= True)