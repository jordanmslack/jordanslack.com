from datetime import date
import requests
import json


def get_years(start, end, r=2):
    return round((start - end).days / 365, r)


def calculate_experience(exp):

    start_date = date(2016, 6, 1)
    today = date.today()
    total_period = get_years(today, start_date)
    experience = {k: [get_years(today, v, 2), get_years(today, v, 2)/total_period * 100] for k, v in exp.items()}

    return experience


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
