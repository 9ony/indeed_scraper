import requests
from bs4 import BeautifulSoup
s_num = 0 
l_num = 50
indeed_results = requests.get(f"https://www.indeed.com/jobs?q=python&limit={l_num}&radius=25&start={s_num}")
indeed_soup = BeautifulSoup(indeed_results.text , 'html.parser')

pagination = indeed_soup.find("ul",{"class": "pagination-list"})
CountPage = indeed_soup.find("div",{"class": "SearchCountPages"})

pages = pagination.find_all('li')
aria_labels = []
for page in pages:
    if page.find("span",{"class":"np"})==None and page.find("b")==None :
        aria_labels.append(page.find("span"))

print(aria_labels)