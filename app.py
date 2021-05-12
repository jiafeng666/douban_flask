from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    #return render_template('index.html')
    return index()


@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect('movie.db')   #连接数据库
    cur = con.cursor()   #游标
    sql = "select * from movie250"  #查询所有信息
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)    #放到一个列表里
    cur.close()
    con.close()

    return render_template('movie.html', movies=datalist)


@app.route('/score')
def score():
    score = []
    num = []
    con = sqlite3.connect('movie.db')   #连接数据库
    cur = con.cursor()   #游标
    sql = "select score,count(score) from movie250 group by score"  #查询所有信息
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])    #放到一个列表里
        num.append(item[1])
    cur.close()
    con.close()
    return render_template('score.html',score=score,num=num)


@app.route('/word')
def word():
    return render_template('word.html')


@app.route('/team')
def team():
    return render_template('team.html')


if __name__ == '__main__':
    app.run()
