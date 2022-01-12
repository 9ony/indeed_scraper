import requests
from bs4 import BeautifulSoup
    
def pages_max_func(start=0):
    URL = f"https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start={start*50}"
    indeed_results = requests.get(URL)
    indeed_soup = BeautifulSoup(indeed_results.text , 'html.parser')
    pagination = indeed_soup.find("ul",{"class": "pagination-list"})
    links = pagination.find_all('li')
    pages = []
    print(start)
    for link in links:
        # if link.find("span").string:
        #     pages.append(int(link.find("a").get('aria-label')))
        if link.find("b"):
            pages.append(int(link.b.get('aria-label')))
        elif link.find("span").string:
            pages.append(int(link.find("a").get('aria-label')))
            # pages.append(int(link.find("span").string))
        # else:
        #     print("검색결과가 없습니다")
        #     break
    max_page=pages[len(pages)-1]
    next_button = pagination.find("a",{"aria-label":"다음"})
    print(pages)
    # for hrefs in pagination.find_all('a'):
    #     if hrefs.get('aria-label')=="다음":
    #         return hrefs.get('href') #이것을 쿼리[a]로 날려줘서 위에 조건문이 안될때까지 반복하면 전체페이지를 스캔할수 있을것같다.
    #     else:
    #         print("다음버튼이 없습니다.")
    if next_button:
        return pages_max_func(max_page)
    else:
        print("다음페이지가 없습니다")
        print("현재페이지는",link.b.get('aria-label'))
        return max_page
print("마지막페이지는=",pages_max_func())