from flask import Blueprint, render_template, Response, make_response, redirect, request, url_for
from sqlalchemy.sql import operators

from App.ext import db
from App.models import TrainLine, TrainTimeTable

blue = Blueprint('blue', __name__)

def init_view(app):
    app.register_blueprint(blue)

@blue.route('/')
def index():
    return render_template('index.html')

@blue.route('/query/', methods=('POST', 'GET'))
def train_query():
    if request.method == 'GET':
        return redirect(url_for('blue.index'))

    elif request.method == 'POST':
        add_depart = request.form.get("add_depart")
        add_arrive = request.form.get("add_arrive")

        lines = TrainLine.query.filter(TrainLine.station_schedule.contains("{}%{}".format(add_depart, add_arrive))).all()
        line_num_list = [line.train_num for line in lines]
        print(line_num_list)
        info_list = []
        for list_num in line_num_list:
            train_type = TrainLine.query.filter(TrainLine.train_num == list_num).first().train_type
            station_depart = TrainTimeTable.query.filter(TrainTimeTable.train_num == list_num).filter(TrainTimeTable.station_name.contains(add_depart)).first()
            station_arrive = TrainTimeTable.query.filter(TrainTimeTable.train_num == list_num).filter(TrainTimeTable.station_name.contains(add_arrive)).first()
            access_train = [train_type, list_num, station_depart.station_name, station_arrive.station_name, station_depart.time_depart, station_arrive.time_arrive]
            info_list.append(access_train)
        query_stations = [add_depart, add_arrive]
        print(info_list)

        return render_template('query.html', info_list=info_list, query_stations=query_stations)







@blue.route('/addtrain/')
def add_train():
    line = TrainLine()

    line.train_type = "高铁"
    line.train_num = "G1"
    line.station_depart = "北京南"
    line.station_arrive = "上海虹桥"
    line.station_schedule = "北京南-济南西-南京南-上海虹桥"

    db.session.add(line)
    db.session.commit()

    return "火车路线添加成功"