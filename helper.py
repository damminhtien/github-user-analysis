import requests


def fetch_user(target_user, authentication):
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


def fetch_lang(target_user, authentication):
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

	data = {}
	data['language_used'] = language_used
	data['times_used'] = times_used
	data['len'] = len(language_used)

	return data
