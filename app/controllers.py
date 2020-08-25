from datetime import date, timedelta
from decouple import config
from flask import render_template, Blueprint

from app.methods import GitHub, calculate_experience


app = Blueprint('app', __name__, url_prefix='')


@app.route("/", methods=['GET', 'POST'])
def home():

    github = GitHub(username=config('GITHUB_USERNAME'), token=config('GITHUB_TOKEN'))
    repos = github.get_repos()

    exp = {
        'Python': date(2017, 11, 15),
        'Javascript': date(2019, 3, 1),
        'SQL': date(2018, 6, 1),
        'CSS': date(2017, 8, 1),
        'HTML': date(2017, 6, 1),
        'Salesforce': date(2017, 3, 18),
    }

    experience = calculate_experience(exp)
    print(experience)

    return render_template('index.html', repos=repos, experience=experience)
