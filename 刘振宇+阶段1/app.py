from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from wtforms.validators import DataRequired
from wtforms import *
from flask_wtf import Form
import Search_json
import sys

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class SearchModel(Form):
    from_station = StringField(validators=[DataRequired()])
    to_station = StringField(validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])
    submit = SubmitField('查询')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchModel()
    if form.date.data is not None:
        from_station = form.from_station.data
        to_station = form.to_station.data
        s_date = form.date.data.strftime('%Y-%m-%d')
        search = Search_json.Ticket(from_station, to_station, s_date)
        search.post_info()
        if search.info['data'] is None:
            flash('没有得到相关的信息,请检查你输入的车站名称,时间!')
        return render_template('12306.html',
                               current_time=datetime.utcnow(),
                               form=form,
                               data_list=search.info['data']
                               )

    return render_template('12306.html',
                           current_time=datetime.utcnow(),
                           form=form,
                           )


if __name__ == '__main__':
    app.run()
