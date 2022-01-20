import time
import random
import requests
from bs4 import BeautifulSoup
LIMIT=50
URL = f"https://kr.indeed.com/취업?q=python&&l=서울&limit={LIMIT}&radius=100&sort=date"

def pages_max_func(start=0):
    start_n=f"&start={start*LIMIT}"
    results = requests.get(URL+start_n)
    time.sleep(random.uniform(2,4))
    soup = BeautifulSoup(results.text , 'html.parser')
    if soup.find("nav",{"role":"navigation"}):
        pagination = soup.find("ul",{"class": "pagination-list"})
        links = pagination.find_all('li')
        pages = []
    
        for link in links:
            if link.find("b"):
                pages.append(int(link.b.get('aria-label')))
            elif link.find("span").string:
                pages.append(int(link.find("a").get('aria-label')))
        
        max_page=pages[len(pages)-1]
        next_button = pagination.find("a",{"aria-label":"다음"})

        if next_button:
            return pages_max_func(max_page)
        else:
            return max_page

    else : 
        return 1 #html내에 페이지를 매기는 섹션이 없을때 1을 반환

def indeed_jobs(last_page):
    page =[] #페이지를 확인하기 위한 배열 변수
    result = []
    for start in range(last_page):
        page.append(start)
        print("현재페이지=",page[len(page)-1]+1)
        job_results = requests.get(URL+f"&start={start*LIMIT}")
        time.sleep(random.uniform(7,10))
        print(job_results.status_code)
        soup = BeautifulSoup(job_results.text,'html.parser')
        jobs = soup.find("div",{"id":"mosaic-provider-jobcards"})
        mobtk = jobs.a.get('data-mobtk')  #mobtk의 attribute를 읽어와서 soup 파라미터에 넣어줌
        # print("Mob-tk="+mobtk) #mob-tk가 맞는지 확인한 임시코드
        job_infos = jobs.find_all("a",{"data-mobtk":f"{mobtk}"})
        locals()['titles_page{}'.format(page[len(page)-1]+1)] = []
        # locals()['snippets_page{}'.format(page[len(page)-1]+1)] = []
        locals()['company_page{}'.format(page[len(page)-1]+1)] = []
        index = [] #몇번째에서 회사명이 에러났는지 확인하기위한 배열
        
        for i,job_info in enumerate(job_infos):
            if job_info.find("span",{"class":"companyName"}) is not None:
                locals()['company_page{}'.format(page[len(page)-1]+1)].append(job_info.find("span",{"class":"companyName"}).string)
            else:
                locals()['company_page{}'.format(page[len(page)-1]+1)].append("회사명없음")
                index.append(i) #파싱오류가난 현재 순서를 인덱스에 저장함
            locals()['titles_page{}'.format(page[len(page)-1]+1)].append(job_info.find("span",{"class":''}).get('title'))
        
            if len(index)>0:
                # errcompany = parser_html[start].find_all("a",{"data-mobtk":f"{mobtk}"})
                for x in range(len(index)):
                    # for errcompany in parser_html[start].find_all("a",{"data-mobtk":f"{mobtk}"}):
                    if job_infos[index[x]].find("span",{"class":"companyName"}) is not None:
                        locals()['company_page{}'.format(page[len(page)-1]+1)][index[x]]=job_infos[index[x]].find("span",{"class":"companyName"}).string
                    else :
                        locals()['company_page{}'.format(page[len(page)-1]+1)][index[x]]="회사명없음"

            result.append(f"회사명 = {locals()['company_page{}'.format(page[len(page)-1]+1)][i]}  타이틀 = {locals()['titles_page{}'.format(page[len(page)-1]+1)][i]}")
        
        print("타이틀")
        print(locals()['titles_page{}'.format(page[len(page)-1]+1)])
        print(len(locals()['titles_page{}'.format(page[len(page)-1]+1)]))
        # print(locals()['snippets_page{}'.format(page[len(page)-1]+1)])
        # print(len(locals()['snippets_page{}'.format(page[len(page)-1]+1)]))
        print("회사명")
        print(locals()['company_page{}'.format(page[len(page)-1]+1)])
        print(len(locals()['company_page{}'.format(page[len(page)-1]+1)]))
    # print(index)
    num = int(input("페이지를 입력하세요"))
    if num>0:
        print(job_infos[num-1].find_all("a",{"data-mobtk":""}))
    else :
        pass
    return result
def job_result(results):
    for result in results:
        print(result)