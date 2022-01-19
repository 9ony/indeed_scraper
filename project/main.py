from indeed import pages_max_func
from indeed import searching_job
max_page = pages_max_func()
search = searching_job(max_page)
print(search[0:50])
print(len(search))