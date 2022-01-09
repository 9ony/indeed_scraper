import requests
from bs4 import BeautifulSoup

indeed_results = requests.get("https://www.indeed.com/jobs?q=python&limit=50&radius=25")
indeed_soup = BeautifulSoup(indeed_results.text , 'html.parser')

print(indeed_soup)
