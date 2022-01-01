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
    os.chdir(REPOSITORY_PATH)
    os.system("mkdir " + repo_name)
    os.chdir(REPOSITORY_PATH + repo_name)
    os.system("git init")
    os.system("git remote add origin https://github.com/" + GITHUB_USER + "/" + repo_name + ".git")
    os.system("echo '# " + repo_name + "' >> README.md")
    os.system("git add . && git commit -m 'Initial Commit' && git push origin master")
except FileExistsError as err:
    raise SystemExit(err)