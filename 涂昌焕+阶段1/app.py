from flask import Flask,render_template,request,flash,redirect,url_for
from os import urandom
from flask_bootstrap import Bootstrap
import pymysql
app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(10)

@app.route('/')
def index():
    return 'hello'


#登陆
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == '123456':
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
        return start+target+date
@app.route('/about')
def about():
    pass

if __name__ == '__main__':
    app.run()
