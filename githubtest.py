from github import Github
import os
from pprint import pprint

token = os.getenv('ded9d9edab875715aa87f5ad8a9c8e35622f7b72', '...')
g = Github(token)
repo = g.get_repo("yukinno/Quento")
issues = repo.get_issues(state="open")
pprint(issues.get_page(0)