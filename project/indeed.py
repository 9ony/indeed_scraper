import requests
from bs4 import BeautifulSoup
LIMIT=50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25&sort=date"
def pages_max_func(start=0):
    start_n=f"&start={start*LIMIT}"
    results = requests.get(URL+start_n)
    soup = BeautifulSoup(results.text , 'html.parser')
    pagination = soup.find("ul",{"class": "pagination-list"})
    links = pagination.find_all('li')
    pages = []
    # print(start)
    for link in links:
        if link.find("b"):
            pages.append(int(link.b.get('aria-label')))
        elif link.find("span").string:
            pages.append(int(link.find("a").get('aria-label')))
        # else:
        #     print("검색결과가 없습니다")
        #     break
    max_page=pages[len(pages)-1]
    next_button = pagination.find("a",{"aria-label":"다음"})
    # print(pages)
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

def searching_job(last_page):
    page =[]
    for start in range(last_page):
        page.append(start)
        print(page)
        print("현재페이지=",page[len(page)-1]+1)
        job_results = requests.get(URL+f"&start={start*LIMIT}")
        soup = BeautifulSoup(job_results.text,'html.parser')
        job_seen_beacon = soup.find_all("div",{"class":"job_seen_beacon"})
        locals()['titles_page{}'.format(page[len(page)-1]+1)] = []
        locals()['snippets_page{}'.format(page[len(page)-1]+1)] = []
        locals()['company_page{}'.format(page[len(page)-1]+1)] = []
        # title = job_seen_beacon.span.get('title')
        # snippet = job_seen_beacon.find("div",{"class":"job-snippet"}).string
        # company = job_seen_beacon.find("span",{"class":"companyName"}).string
        #페이지별 title,snippet {LIMIT}개를 담을 동적변수 선언
        #   지역변수면 locals() , 전역변수면 globals() [변수명{(.format의숫자가 들어옴).format(x)}]
        for job_info in job_seen_beacon:
            locals()['titles_page{}'.format(page[len(page)-1]+1)].append(job_info.find("span").get('title'))
            # locals()['snippets_page{}'.format(start_n+1)].append(job_info.find("div",{"class":"jot-snippet"}).string)
            locals()['company_page{}'.format(page[len(page)-1]+1)].append(job_info.find("span",{"class":"companyName"}).string)
        print(locals()['titles_page{}'.format(page[len(page)-1]+1)])
        print(len(locals()['titles_page{}'.format(page[len(page)-1]+1)]))
        # print(locals()['snippets_page{}'.format(page[len(page)-1]+1)])
        print(locals()['company_page{}'.format(page[len(page)-1]+1)])
    # print(job_seen_beacon)
        # for title in job_seen_beacon:
# div,"class=":"job_seen_beacon" 안에 h2,"class":"jobtitle" 과 div,"class":"job-snippet"(부서설명?)가져오기
# print("마지막페이지는=",pages_max_func())