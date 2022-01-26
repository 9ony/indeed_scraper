import time
import random
import requests
from save import save_file
from bs4 import BeautifulSoup
LIMIT = 50
site = 'https://kr.indeed.com'
URL = f"{site}/취업?q=python&&l=서울&limit={LIMIT}&radius=100&sort=date"

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
    # result = {}
    for start in range(last_page):
        page.append(start)
        print("Scrapping page",page[len(page)-1]+1)
        job_results = requests.get(URL+f"&start={start*LIMIT}")
        time.sleep(random.uniform(7,10))
        print(job_results.status_code)
        soup = BeautifulSoup(job_results.text,'html.parser')
        jobs = soup.find("div",{"id":"mosaic-provider-jobcards"})
        mobtk = jobs.a.get('data-mobtk')  #mobtk의 attribute를 읽어와서 soup 파라미터에 넣어줌
        # print("Mob-tk="+mobtk) #mob-tk가 맞는지 확인한 임시코드
        job_infos = jobs.find_all("a",{"data-mobtk":f"{mobtk}"})
        for job_info in job_infos:
            # print(test(job_info).values)
            save_file(test(job_info))
        
def test(data):
    companytitle = data.find("span",{"class":''}).get('title')
    companyName = data.find("span",{"class":"companyName"})
    companyLocation = data.find("div",{"class":"companyLocation"}).string
    companyLink = site+data.get('href')
    if companyName is not None:
        companyName = companyName.string
    else:
        companyName = "헤드헌트"
    return {'회사명' : companyName, '타이틀' : companytitle, '위치' : companyLocation, '링크' : companyLink}