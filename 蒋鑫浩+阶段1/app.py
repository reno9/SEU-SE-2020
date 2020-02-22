from flask import Flask, render_template, flash, request
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from wtforms.validators import DataRequired
from wtforms import *
from flask_wtf import Form

app = Flask(__name__)
manage = Manager(app)
bootsrap = Bootstrap(app)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/train12306'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_CHECK_DEFAULT'] = False
db = SQLAlchemy(app)
app.secret_key = 'gslavine'


class Train(db.Model):
    __tablename__ = 'trains'
    id = db.Column(db.String(10), nullable=False, primary_key=True)
    from_station = db.Column(db.String(100), nullable=False)
    to_station = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.TIME, nullable=False)
    arrive_time = db.Column(db.TIME, nullable=False)
    date = db.Column(db.DATE)


class SearchModel(Form):
    from_station = StringField(validators=[DataRequired()])
    to_station = StringField(validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])
    submit = SubmitField('查询')


@app.route('/', methods=['GET', 'POST'])
def index():
    trains = {}
    Search_form = SearchModel()
    if Search_form.date.data is not None:
        from_station = Search_form.from_station.data
        to_station = Search_form.to_station.data
        date = Search_form.date.data
        trains = Train.query.order_by(Train.start_time).filter(Train.from_station == from_station, Train.to_station == to_station,
                                    Train.date == date).all()
        if trains:
           pass
        else:
            if request.method == 'POST':
                flash('没有得到相关的信息,请检查你输入的车站名称,时间!')
    return render_template('index.html', form=Search_form, data_list=trains, current_time=datetime.utcnow(), )


if __name__ == '__main__':
    app.run()
