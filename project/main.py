from indeed import pages_max_func
from indeed import indeed_jobs
from indeed import job_result
max_page = pages_max_func()
search = indeed_jobs(max_page)
print(search)
print(len(search))
job_result(search)