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