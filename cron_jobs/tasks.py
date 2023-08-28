
import subprocess

def pull_from_github():
    subprocess.run(['git', 'pull', 'origin', 'main'])
