import requests
from bs4 import BeautifulSoup

indeed_results = requests.get("https://www.indeed.com/jobs?q=python&limit=50&radius=25&start=0")
indeed_soup = BeautifulSoup(indeed_results.text , 'html.parser')

pagination = indeed_soup.find("ul",{"class": "pagination-list"})


pages = pagination.find_all('li')
aria_labels = []
for page in pages:
    if None!=page.find("b"):
        aria_labels.append(page.find("b"))

print(aria_labels)