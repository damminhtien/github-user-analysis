from flask import Flask, request, render_template, redirect
import requests
import json
from setting import username, password
from requests.auth import HTTPBasicAuth


app = Flask(__name__)
authentication = HTTPBasicAuth(username, password)
target_user = 'damminhtien'


@app.route('/')
def index():
	data = {}
	try:
	    user_data = requests.get('https://api.github.com/users/' + target_user, auth = authentication).json()
	    data['user'] = {}
	    data['user']['login'] = user_data['login']
	    data['user']['name'] = user_data['name']
	    data['user']['avatar_url'] = user_data['avatar_url']
	    data['user']['company'] = user_data['company']
	    data['user']['bio'] = user_data['bio']
	    data['user']['public_repos'] = user_data['public_repos']
	    data['user']['followers'] = user_data['followers']
	    data['user']['following'] = user_data['following']
	    data['user']['created_at'] = user_data['created_at']
	except Exception as e:
		return str(e)

	return render_template('index.html', data=data)


app.run(use_debugger= True, debug= True)