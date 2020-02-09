from flask import Flask,render_template,request,flash,redirect,url_for
from os import urandom
from query.query import query,station_info
from flask_bootstrap import Bootstrap
import pymysql
import json
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = urandom(10)

@app.route('/')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin@163.com' and password == '123456':
            return redirect(url_for('search'))
            # return render_template('search.html')

        else:
            flash('登陆失败,请检查后再次登陆')
            return redirect(url_for('login'))

#搜索
@app.route('/search',methods=['GET','POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    if request.method == 'POST':
        start = request.form.get('start')
        target = request.form.get('target')
        date = request.form.get('date')
        station = station_info()
        start_code = station[start]
        target_code = station[target]
        find_result = query(date,start_code,target_code)

        # 获取result
        json_result  = json.loads(find_result)["data"]['result']

        f = open("station.txt", "r")
        fs = f.read()
        code_dict = {v: k for k, v in eval(fs).items()}
        tickets = []
        for ticket in json_result:
            ticket_list = ticket.split("|")
            checi = ticket_list[3]
            from_code = ticket_list[6]
            from_station = code_dict[from_code]

            to_code = ticket_list[7]
            to_station = code_dict[to_code]

            from_time = ticket_list[8]
            to_time = ticket_list[9]
            total_time = ticket_list[10]
            sp = ticket_list[32] or '--'
            yideng = ticket_list[31] or '--'
            erdeng = ticket_list[30] or '--'
            gaoji_ruanwo = ticket_list[21] or '--'
            yideng_ruanwo = ticket_list[23] or '--'
            erdeng_ruanwo = ticket_list[28] or '--'
            dongwo = ticket_list[33] or '--'
            yingzuo = ticket_list[29] or '--'
            wuzuo = ticket_list[26] or '--'
            qita = '--'

            tickets.append([checi,from_station,to_station,from_time,to_time,total_time,sp,yideng,erdeng,gaoji_ruanwo,yideng_ruanwo,dongwo,erdeng_ruanwo,yingzuo,wuzuo,qita])
        for p in tickets:
            print(p)
        return render_template('index.html', u=tickets)

@app.route('/about')
def about():
    pass

if __name__ == '__main__':
    app.run()
