import time
import random
import requests
from bs4 import BeautifulSoup
LIMIT=50
URL = f"https://kr.indeed.com/취업?q=Python&&l=서울&limit={LIMIT}&radius=100&sort=date"
# URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=Python&l=%EC%84%9C%EC%9A%B8&limit=50&radius=25&start=9999&vjk=50483549cea811b8"
def pages_max_func(start=0):
    start_n=f"&start={start*LIMIT}"
    results = requests.get(URL+start_n)
    time.sleep(random.uniform(2,4))
    soup = BeautifulSoup(results.text , 'html.parser')
    if soup.find("nav",{"role":"navigation"}):
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
            # print("다음페이지가 없습니다")
            # print("현재페이지는",link.b.get('aria-label'))
            return max_page

    else :
        return 1
def searching_job(last_page):
    page =[]
    # lists=[]
    # lists2=[]
    for start in range(last_page):
        page.append(start)
        # print(page)
        print("현재페이지=",page[len(page)-1]+1)
        # job_results = requests.get(URL+f"&start={start*LIMIT+9999}")
        job_results = requests.get(URL+f"&start={start*LIMIT}")
        time.sleep(random.uniform(5,8))
        print(job_results.status_code)
        soup = BeautifulSoup(job_results.text,'html.parser')
        jobs = soup.find("div",{"id":"mosaic-provider-jobcards"})
        # job_seen_beacon = jobs.find_all("div",{"class":"job_seen_beacon"})
        mobtk = jobs.a.get('data-mobtk') 
        #mobtk의 attribute를 읽어와서 soup 파라미터에 넣어줌
        print("Mob-tk="+mobtk)
        job_infos = jobs.find_all("a",{"data-mobtk":f"{mobtk}"})
        locals()['titles_page{}'.format(page[len(page)-1]+1)] = []
        # locals()['snippets_page{}'.format(page[len(page)-1]+1)] = []
        locals()['company_page{}'.format(page[len(page)-1]+1)] = []
        #페이지별 title,snippet {LIMIT}개를 담을 동적변수 선언
        #지역변수면 locals() , 전역변수면 globals() [변수명{(.format의숫자가 들어옴).format(x)}]
        
        for job_info in job_infos:
            # newjob = job_info.find("h2",{"class":"jobTitle jobTitle-newJob"})
            # newjob2 = job_info.h2.get('class')
            # if newjob2 == ['jobTitle', 'jobTitle-color-purple', 'jobTitle-newJob']:
            #     lists.append(newjob2)
            # else :
            #     lists2.append(newjob2)
            # locals()['titles_page{}'.format(page[len(page)-1]+1)].append(job_info.find('span','').get('title'))
            # locals()['titles_page{}'.format(page[len(page)-1]+1)].append(job_info.find("span",{"class":''}).get('title'))
            # locals()['snippets_page{}'.format(start_n+1)].append(job_info.find("div",{"class":"jot-snippet"}).string)
            if job_info.find("span",{"class":"companyName"}):
                locals()['company_page{}'.format(page[len(page)-1]+1)].append(job_info.find("span",{"class":"companyName"}).string)
            else:
                # locals()['company_page{}'.format(page[len(page)-1]+1)].append(job_info.find("a",{"data-tn-element":"companyName"}).string)
                locals()['company_page{}'.format(page[len(page)-1]+1)].append("에러입니다")
        
        # print(locals()['titles_page{}'.format(page[len(page)-1]+1)])
        # print(len(locals()['titles_page{}'.format(page[len(page)-1]+1)]))
        # print(locals()['snippets_page{}'.format(page[len(page)-1]+1)])
        # print(len(locals()['snippets_page{}'.format(page[len(page)-1]+1)]))
        print(locals()['company_page{}'.format(page[len(page)-1]+1)])
        print(len(locals()['company_page{}'.format(page[len(page)-1]+1)]))
        # print(lists)
        # print(len(lists))
        # print(lists2)
        # print(len(lists2))

# div,"class=":"job_seen_beacon" 안에 h2,"class":"jobtitle" 과 div,"class":"job-snippet"(부서설명?)가져오기