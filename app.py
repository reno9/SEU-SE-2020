import json

from flask import Flask, render_template, request
from flask_script import Manager
from utils.spider import city, query
from flask_bootstrap import Bootstrap


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        local = request.form['local']
        destination = request.form['destination']
        times = request.form['times']
        result = city()
        local = result[local]
        destination = result[destination]
        find_result = query(times,local, destination)
        raw_trains = json.loads(find_result)["data"]["result"]
        f = open("station.txt", "r")
        fs = f.read()
        code_dict = {v: k for k, v in eval(fs).items()}
        info_list = []
        for raw_train in raw_trains:
            # 循环遍历每辆列车的信息
            print(raw_train)
            data_list = raw_train.split('|')
            # 车次号码
            train_no = data_list[3]
            # 出发站
            from_station_code = data_list[6]
            from_station_name = code_dict[from_station_code]
            # 终点站
            to_station_code = data_list[7]
            to_station_name = code_dict[to_station_code]
            # 出发时间
            start_time = data_list[8]
            # 到达时间
            arrive_time = data_list[9]
            # 总耗时
            time_fucked_up = data_list[10]
            # 一等座
            first_class_seat = data_list[31] or '--'
            # 二等座
            second_class_seat = data_list[30] or '--'
            # 软卧
            soft_sleep = data_list[23] or '--'
            # 硬卧
            hard_sleep = data_list[28] or '--'
            # 硬座
            hard_seat = data_list[29] or '--'
            # 无座
            no_seat = data_list[26] or '--'

            # 打印查询结果
            # info_list.append(info)
            info = {"ccmc": train_no, "cfz": from_station_name, "zdz": to_station_name, "cfsj": start_time,
                    "ddsj": arrive_time, "zhs": time_fucked_up, "ydz": first_class_seat, "edz": second_class_seat,
                    "rw": soft_sleep, "yw": hard_sleep, "yz": hard_seat, "wz": no_seat}

            info_list.append(info)
        return render_template('index.html',info_list=info_list)

    if request.method == "GET":
        return render_template('submission.html')


if __name__ == '__main__':
    app.run()
