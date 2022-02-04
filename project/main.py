# from indeed import *
from indeed import pages_max_func
from indeed import indeed_jobs
# from indeed_test2 import job_result
max_page = pages_max_func()
search = indeed_jobs(max_page)
# print(search)
# print(len(search))
# print(job_result(search))