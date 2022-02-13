from flask import redirect, render_template , Flask , request , Response , send_file
from indeed import pages_max_func
from indeed import indeed_jobs
from save import save_file
import sys

app = Flask("Scrapper")

# @app.route('/')
# def start():
#     return "hello"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/report')
def report():
    
    word = request.args.get('word')
    #word가 공백이거나 특수문자로만 이루어져있을때 word에 null을 할당
    if ''.join(filter(str.isalnum,word))=="" or word.strip(' ')=="":
        word = "null"
    if word != "null":
        word = word.lower()
        word = ''.join(filter(str.isalnum,word))
        URL = f"/취업?q={word}&l=서울&limit=50&radius=100&sort=date"
        save_file(0,word)
        max_page = pages_max_func(0,URL)
        jobs = indeed_jobs(max_page , URL , word)
    else:
        return redirect('/')
    return render_template("report.html" ,
     search=word,
     resultslen=len(jobs),
     results = jobs
     )
app.run(host="127.0.0.1",port=5000)
# print(sys.path)