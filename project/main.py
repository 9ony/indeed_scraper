import requests
from bs4 import BeautifulSoup

s_num = 0 
l_num = 50
indeed_results = requests.get(f"https://www.indeed.com/jobs?q=python&limit={l_num}&radius=25&start={s_num}")
indeed_soup = BeautifulSoup(indeed_results.text , 'html.parser')

pagination = indeed_soup.find("ul",{"class": "pagination-list"})
CountPage = indeed_soup.find("div",{"class": "SearchCountPages"})

links = pagination.find_all('li')
pages = []
for link in links:
    if link.find("span",{"class":"np"})==None and link.find("b")==None :
    #Span(태그)안에  클래스명이 np인것과 b태그가 아닌것만 pages배열에 넣어주는 조건
    #위조건이 없을시엔 pages[1:-1]<<배열에있는값을 2번째부터 마지막것을 제외하고 출력할수 있지만
    #지금현재 페이지가 1부터 20까지 다뜨는게아니고 넥스트페이지라는 버튼이있기때문이고 자기현재페이지가 중간으로 되있어서
    #순서대로할시 ex) 1,2,<span class:np>3</span>,4,5 이렇게 출력됨
    #이를방지하기위해 배열파라미터에 값을 지정안해주고 아예 조건문으로 값을 지정해서 넣어줌
        pages.append(int(link.find("span").string))

print(pages)