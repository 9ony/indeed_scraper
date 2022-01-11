import requests
from bs4 import BeautifulSoup
    
def pages_max_fuc(q=f"/jobs?q=python&limit=50&radius=25&start=0"):
    indeed_results = requests.get("https://kr.indeed.com"+q)
    indeed_soup = BeautifulSoup(indeed_results.text , 'html.parser')
    pagination = indeed_soup.find("ul",{"class": "pagination-list"})
    links = pagination.find_all('li')

    pages = []
    for link in links:
        #Span(태그)안에  클래스명이 np인것과 b태그가 아닌것만 pages배열에 넣어주는 조건
        #위조건이 없을시엔 pages[1:-1]<<배열에있는값을 2번째부터 마지막것을 제외하고 출력할수 있지만
        #지금현재 페이지가 1부터 20까지 다뜨는게아니고 넥스트페이지라는 버튼이있기때문이고 자기현재페이지가 중간으로 되있어서
        #순서대로할시 ex) 1,2,<span class:np>3</span>,4,5 이렇게 출력됨
        #이를방지하기위해 배열파라미터에 값을 지정안해주고 아예 조건문으로 값을 지정해서 넣어줌
            max_page = 0
            if link.find("b"):
                    pages.append(int(link.b.string))
                    if max_page<pages[len(pages)-1]:
                        return max(max_page,pages[len(pages)-1])
            elif link.find("span").string!=None:
                pages.append(int(link.find("span").string))
            else:
                print("아아아아아아님")
    print(pages)
    print(max_page)
    for hrefs in pagination.find_all('a'):
        if hrefs.get('aria-label')=="다음":
            return hrefs.get('href') #이것을 쿼리[a]로 날려줘서 위에 조건문이 안될때까지 반복하면 전체페이지를 스캔할수 있을것같다.
        else:
            print("다음버튼이 없습니다.")
            break
print(pages_max_fuc())