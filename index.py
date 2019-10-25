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
		base_url = 'https://api.github.com/users/' + target_user + '/repos'
		url = base_url
		page_no = 1
		repos_data = []
		while (True):
		    response = requests.get(url, auth = authentication)
		    response = response.json()
		    repos_data = repos_data + response
		    repos_fetched = len(response)
		    print(page_no)
		    if (repos_fetched == 30):
		        page_no = page_no + 1
		        url = base_url + '?page=' + str(page_no)
		    else:
		        break

		_language_ignore = ['HTML', 'CSS', 'Jupyter Notebook']
		language_used = []
		total_times = 0
		times_used = []

		for rd in repos_data:
			print(rd['name'])
			if rd['fork']: continue
			response = requests.get(rd['languages_url'], auth = authentication)
			response = response.json()
			language_rd = list(response.keys())
			for l in language_rd:
				if l in _language_ignore: continue
				if l not in language_used: 
					language_used.append(l)
					times_used.append(response[l])
				else:
					times_used[language_used.index(l)] = times_used[language_used.index(l)] + response[l]
				total_times += response[l]

		for i in range(len(language_used)):
			times_used[i] /= total_times

		data['lang'] = {}
		data['lang']['language_used'] = language_used
		data['lang']['times_used'] = times_used
		data['lang']['len'] = len(language_used)
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
		base_url = 'https://api.github.com/users/' + target_user + '/repos'
		url = base_url
		page_no = 1
		repos_data = []
		while (True):
		    response = requests.get(url, auth = authentication)
		    response = response.json()
		    repos_data = repos_data + response
		    repos_fetched = len(response)
		    print(page_no)
		    if (repos_fetched == 30):
		        page_no = page_no + 1
		        url = base_url + '?page=' + str(page_no)
		    else:
		        break

		_language_ignore = ['HTML', 'CSS', 'Jupyter Notebook']
		language_used = []
		total_times = 0
		times_used = []

		for rd in repos_data:
			print(rd['name'])
			if rd['fork']: continue
			response = requests.get(rd['languages_url'], auth = authentication)
			response = response.json()
			language_rd = list(response.keys())
			for l in language_rd:
				if l in _language_ignore: continue
				if l not in language_used: 
					language_used.append(l)
					times_used.append(response[l])
				else:
					times_used[language_used.index(l)] = times_used[language_used.index(l)] + response[l]
				total_times += response[l]

		for i in range(len(language_used)):
			times_used[i] /= total_times

		data['lang'] = {}
		data['lang']['language_used'] = language_used
		data['lang']['times_used'] = times_used
		data['lang']['len'] = len(language_used)
	except Exception as e:
		error['fetch_lang'] = str(e)

	return return_template('index.html', data=data, error=error)

app.run(use_debugger= True, debug= True)