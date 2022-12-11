#!/usr/bin/env python3

# Load packages
import argparse
import os
import requests

# Load Tokens
from Git_Token import TOKEN
from Git_Token import REPOSITORY_PATH
from Git_Token import GITHUB_USER
# from pprint import pprint (testing purposes)

# Command Line switches
input_text = argparse.ArgumentParser()
input_text.add_argument("--name", "-n", type=str, dest="name", required=True)
input_text.add_argument("--private", "-p", dest="is_private", action="store_true")
user_entry = input_text.parse_args()
repo_name = user_entry.name
is_private = user_entry.is_private

#Read the path from Git Token file
# REPO_PATH = "/Users/USER/"
# GITHUB_USER = 'github_user'
GITHUB_URL = "https://api.github.com"

if is_private:
    payload = '{"name": "' + repo_name + '", "private": true }'
else:
    payload = '{"name": "' + repo_name + '", "private": false }'

headers = {
    "Authorization": "token " + TOKEN,
    "Accept": "application/vnd.github.v3+json"
}

# Create repo
try:
    r = requests.post(GITHUB_URL + "/user/repos", data=payload, headers=headers)
    r.raise_for_status()
    # pprint(r.json())
except requests.exceptions.RequestException as err:
    raise SystemExit(err)

try:  
    os.chdir(REPOSITORY_PATH) # move to repository path
    os.system("mkdir " + repo_name) # Create the folder with the repo name
    os.chdir(REPOSITORY_PATH + repo_name) # Move to repo folder
    os.system("mkdir app") # Create an app folder
    os.system("mkdir data") # Create a data folder
    os.system("mkdir figs") # Create a fig folder
    os.system("mkdir docs") # Create a documentation folder
    os.system("mkdir src") # Create a source code folder
    os.system("mkdir report") # Create a report folder
    os.chdir(REPOSITORY_PATH + repo_name + "/app") # Move to app folder
    os.system("mkdir www") # Create www folder folder
    os.system("mkdir rds") # Create rds folder folder
    os.system("mkdir utils") # Create an report folder
    os.system("touch ui.R ") # Create UI file
    os.system("touch server.R ") # Create server file
    os.system("touch global.R ") # Create global file
    os.chdir(REPOSITORY_PATH + repo_name) # Move to repo folder
    os.system("git init")
    os.system("git remote add origin https://github.com/" + GITHUB_USER + "/" + repo_name + ".git")
    os.system("echo '# " + repo_name + "' >> README.md") # Create Readme file
    os.system("echo '.DS_Store' >> .gitignore") # Create gitignore and add file
    os.system("echo '.RData' >> .gitignore") # Add RData to gitignore file
    os.system("echo '.Rhistory' >> .gitignore") # Add Rhistory to gitignore file
    os.system("echo '.Renviron' >> .gitignore") # Add Renviron to gitignore file
    os.system("echo '/app/rsconnect/' >> .gitignore") # Add app/rsconnect to gitignore file
    os.system("echo '/app/.Renviron' >> .gitignore") # Add app/Renviron to gitignore file
    os.system("git add . && git commit -m 'Initial Commit' && git push origin master")
except FileExistsError as err:
    raise SystemExit(err)