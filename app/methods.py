import requests
import json


class GitHub:

    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.auth = (self.username, self.token)
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
        }

    def get_repos(self):

        url = f'https://api.github.com/users/{self.username}/repos'
        response = requests.get(url, headers=self.headers)
        data = json.loads(response.content)

        return data
