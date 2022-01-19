from ast import Del
import time
import random
import requests
from bs4 import BeautifulSoup
LIMIT=50
URL = f"https://kr.indeed.com/취업?q=python&&l=서울&limit={LIMIT}&radius=100&sort=date"
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
    parser_html=[]
    result = []
    for start in range(last_page):
        page.append(start)
        # print(page)
        print("현재페이지=",page[len(page)-1]+1)
        # job_results = requests.get(URL+f"&start={start*LIMIT+9999}")
        job_results = requests.get(URL+f"&start={start*LIMIT}")
        time.sleep(random.uniform(7,10))
        print(job_results.status_code)
        soup = BeautifulSoup(job_results.text,'html.parser')
        jobs = soup.find("div",{"id":"mosaic-provider-jobcards"})
        parser_html.append(jobs)
        # job_seen_beacon = jobs.find_all("div",{"class":"job_seen_beacon"})
        mobtk = jobs.a.get('data-mobtk') 
        #mobtk의 attribute를 읽어와서 soup 파라미터에 넣어줌
        print("Mob-tk="+mobtk)
        job_infos = jobs.find_all("a",{"data-mobtk":f"{mobtk}"})
        locals()['titles_page{}'.format(page[len(page)-1]+1)] = []
        # locals()['snippets_page{}'.format(page[len(page)-1]+1)] = []
        locals()['company_page{}'.format(page[len(page)-1]+1)] = []
        locals()['error_checkpage{}'.format(page[len(page)-1]+1)] = []
        #페이지별 title,snippet {LIMIT}개를 담을 동적변수 선언
        #지역변수면 locals() , 전역변수면 globals() [변수명{(.format의숫자가 들어옴).format(x)}]
        # index = []
        for i,job_info in enumerate(job_infos):
            # newjob = job_info.find("h2",{"class":"jobTitle jobTitle-newJob"})
            # newjob2 = job_info.h2.get('class')
            # if newjob2 == ['jobTitle', 'jobTitle-color-purple', 'jobTitle-newJob']:
            #     lists.append(newjob2)
            # else :
            #     lists2.append(newjob2)
            # locals()['titles_page{}'.format(page[len(page)-1]+1)].append(job_info.find('span','').get('title'))
            # locals()['error_checkpage{}'.format(page[len(page)-1]+1)].append(job_info.contents)
            # locals()['snippets_page{}'.format(start_n+1)].append(job_info.find("div",{"class":"jot-snippet"}).string)
            if job_info.find("span",{"class":"companyName"}) is not None:
                locals()['company_page{}'.format(page[len(page)-1]+1)].append(job_info.find("span",{"class":"companyName"}).string)
            else:
                # locals()['company_page{}'.format(page[len(page)-1]+1)].append(job_info.find("a",{"data-tn-element":"companyName"}).string)
                # job_infos.__getattribute__(job_info.find("span",{"class":"companyName"}).string)
                locals()['company_page{}'.format(page[len(page)-1]+1)].append("!!파싱오류!!")
                # index.append(i)
            locals()['titles_page{}'.format(page[len(page)-1]+1)].append(job_info.find("span",{"class":''}).get('title'))
        # if "!!파싱오류!!" in locals()['company_page{}'.format(page[len(page)-1]+1)]:
        #     print("파싱오류났음")
        #     if len(index)>0:
        #         errcompany = parser_html[start].find_all("a",{"data-mobtk":f"{mobtk}"})
        #         for x in range(len(index)):
        #             # for errcompany in parser_html[start].find_all("a",{"data-mobtk":f"{mobtk}"}):
        #             if errcompany[index[x]].find("span",{"class":"companyName"}) is not None:
        #                 locals()['company_page{}'.format(page[len(page)-1]+1)][index[x]]=errcompany[index[x]].find("span",{"class":"companyName"}).string
        #             else :
        #                 locals()['company_page{}'.format(page[len(page)-1]+1)][index[x]]="회사명없음"
            result.append(f"회사명 = {locals()['company_page{}'.format(page[len(page)-1]+1)][i]}  타이틀 = {locals()['titles_page{}'.format(page[len(page)-1]+1)][i]}")
        
        print("타이틀")
        print(locals()['titles_page{}'.format(page[len(page)-1]+1)])
        print(len(locals()['titles_page{}'.format(page[len(page)-1]+1)]))
        # print(locals()['snippets_page{}'.format(page[len(page)-1]+1)])
        # print(len(locals()['snippets_page{}'.format(page[len(page)-1]+1)]))
        print("회사명")
        print(locals()['company_page{}'.format(page[len(page)-1]+1)])
        print(len(locals()['company_page{}'.format(page[len(page)-1]+1)]))
        # print("파싱데이터")
        # print(locals()['error_checkpage{}'.format(page[len(page)-1]+1)])
        # print(len(locals()['error_checkpage{}'.format(page[len(page)-1]+1)]))
            # print(lists)
            # print(len(lists))
            # print(lists2)
            # print(len(lists2))
        # print(locals()['company_page1'][49])
    # print(index)
    # num = int(input("페이지를 입력하세요"))
    # print(parser_html[num-1].find_all("a",{"data-mobtk":""}))
    return result
# div,"class=":"job_seen_beacon" 안에 h2,"class":"jobtitle" 과 div,"class":"job-snippet"(부서설명?)가져오기