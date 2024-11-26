import requests

token = 'your_personal_access_token'

base_url = 'https://api.github.com/'

headers = {'Authorization': f'token {token}'}

def search_repositories(query):
    url = f"{base_url}search/repositories?q={query}&sort=stars&order=desc"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

data = search_repositories('machine learning')
if data:
    print(data)
