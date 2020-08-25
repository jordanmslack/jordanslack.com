from decouple import config
from flask import render_template, Blueprint

from app.methods import GitHub


app = Blueprint('app', __name__, url_prefix='')


@app.route("/", methods=['GET', 'POST'])
def home():

    github = GitHub(username=config('GITHUB_USERNAME'), token=config('GITHUB_TOKEN'))
    repos = github.get_repos()

    return render_template('index.html', repos=repos)



