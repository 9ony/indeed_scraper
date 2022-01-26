# from indeed import job_result

import csv

    # f = open("joblist.csv", mode="w" newline='')
    # data=['회사명','타이틀','위치','링크']
    # csv.writer(f).writerow(test)
    # f.close()
    # r = open("joblist.csv", mode="r")
    # rd = csv.reader(r)
    # for line in r:
    #     print(line)
    # r.close()
    # return f
def save_file(test):
    if test == 0:
        with open('joblist.csv','w',newline='', encoding='utf-8-sig') as csvfile:
            w = csv.DictWriter(csvfile, fieldnames=['회사명','타이틀','위치','링크'])
            w.writeheader()
            csvfile.close()
        print("csv 초기화")
    else:
        with open('joblist.csv','a',newline='', encoding='utf-8-sig') as csvfile:
            w = csv.DictWriter(csvfile, fieldnames=['회사명','타이틀','위치','링크'])
            w.writerow(test)
            csvfile.close()