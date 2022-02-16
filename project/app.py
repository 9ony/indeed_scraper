from re import search, template
from flask import redirect, render_template , Flask , request , Response , send_file
from indeed import pages_max_func
from indeed import indeed_jobs
from save import save_file
import sys,re

app = Flask("Scrapper")
db={}

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
        word = re.sub(r"[^a-zA-Z0-9'`_-]","",word)
        samedb = db.get(word)
        if  samedb:
            jobs=samedb
        else:   
            URL = f"/취업?q={word}&l=서울&limit=50&radius=100&sort=date"
            max_page = pages_max_func(0,URL)
            jobs = indeed_jobs(max_page , URL , word)
            db[word] = jobs
    else:
        return redirect('/')
    return render_template("report.html" ,
     search=word,
     resultslen=len(jobs),
     results = db[word]
     )
@app.route('/download')
def download():
    word = request.args.get('word')
    if db[word] is "null":
        return redirect('/')
    else :
        # file_name = f"C:\Users\82104\Desktop\웹스크래퍼\joblist.csv"
        file_name = f"{word}_joblist.csv"
    return send_file(file_name,mimetype='text/csv',attachment_filename=f"{word}_joblist.csv",as_attachment=True)

app.run(host="127.0.0.1",port=5000)
# print(sys.path)