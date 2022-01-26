from indeed import pages_max_func
from indeed import indeed_jobs
from save import save_file
# from indeed_test2 import job_result
max_page = pages_max_func()
save_file(0)
search = indeed_jobs(max_page)

# print(search)
# print(len(search))
# print(job_result(search))