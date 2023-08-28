from git import Repo

def pull_from_github():
    repo = Repo('https://github.com/Onimisea/saydi-api.git')  # Replace with the actual path to your repository
    origin = repo.remote('origin')
    origin.pull()
