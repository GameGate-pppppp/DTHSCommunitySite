from tkinter.tix import PopupMenu
from flask import Flask, flash, redirect, render_template, request, url_for
import time

app = Flask(__name__)
app.secret_key = 'helloDongtan'

Posts = []#{"id":"","title":"","content":"","tags":"","date":""}
ID = 0

@app.route("/")
def mainpage():
	return render_template("MainPage.html", Posts=Posts, ID=ID)

@app.route("/board")
def board():
	return render_template("board.html", Posts=Posts, ID=ID)

@app.route("/notice")
def notice():
	return render_template("notice.html")

@app.route("/introduce")
def introduce():
    return render_template("학교소개.html")

@app.route("/post/write", methods=['GET','POST'])
def postWrite():
    if(request.method == 'GET'):
        return render_template("postWrite.html")
        #return render_template("test.html")
    
    elif(request.method == 'POST'):
        global ID
        
        title= request.form['title']
        content= request.form['content']
        tags=request.form['tags']
        date=time.strftime('%Y-%m-%d', time.localtime(time.time()))
        Posts.append({"id":ID,"title":str(title),"content":str(content),"tags":str(tags),"date":str(date)})
        #author=request.form['author']
        #return str(Posts)
        ID += 1
        return redirect('../')
    
@app.route("/post/read", methods=['GET'])
def postRead():
    postId = int(request.args.get('postId'))

    for post in Posts:
        if (post['id'] == postId):
            return render_template("viewPost.html", post = post)

    return 'Not Found'

@app.route("/notice/read", methods=['GET'])
def noticeRead():
    postId = int(request.args.get('postId'))

    if postId == 1:
        return render_template("공지사항(7월급식).html") 
    elif postId == 2:
        return render_template("공지사항(학사일정).html") 
    elif postId == 3:
        return render_template("공지사항(모의고사).html")
    elif postId == 4:
        return render_template("공지사항(시간표).html")
    return 'Not Found'

if __name__ == "__main__":
	app.run(debug=True) 