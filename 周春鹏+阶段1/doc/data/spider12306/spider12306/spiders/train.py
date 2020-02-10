# -*- coding: utf-8 -*-
import time

import pymysql
import scrapy
from flask import json

from spider12306.items import TrainLine, TimeTable


class TrainSpider(scrapy.Spider):
    name = 'train'
    #start_urls = ['https://kyfw.12306.cn/otn/queryTrainInfo/query?leftTicketDTO.train_no=040000266844&leftTicketDTO.train_date=2020-02-09&rand_code=']

    def start_requests(self):
        db = pymysql.connect(host='localhost', user='root', passwd='111', db='TrainQuery', charset='utf8')
        cursor = db.cursor()
        cursor.execute("SELECT no FROM train_num_no")
        result = cursor.fetchall()
        db.close()
        new_result = []
        for item in result:
            if item[0] not in new_result:
                new_result.append(item[0])
        for train_no in new_result:
            url = "https://kyfw.12306.cn/otn/queryTrainInfo/query?leftTicketDTO.train_no={}&leftTicketDTO.train_date=2020-02-10&rand_code=".format(train_no)
            time.sleep(0.8)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        train_dict = json.loads(response.body_as_unicode())
        if train_dict['httpstatus'] == 200 and train_dict['data']['data']:

            train_item = TrainLine()
            time_table_item = TimeTable()
            data_list = train_dict['data']['data']

            if data_list[0]['station_train_code'] == data_list[-1]['station_train_code']:
                train_item['train_num'] = data_list[0]['station_train_code']
            else:
                train_item['train_num'] = data_list[0]['station_train_code'] + '/' + data_list[-1]['station_train_code']
            train_item['train_type'] = data_list[0]['train_class_name']
            train_item['station_depart'] = data_list[0]['start_station_name']
            train_item['station_arrive'] = data_list[0]['end_station_name']
            route = ""
            for s_item in data_list:
                route = route + s_item['station_name'] + "-"
            train_item['station_schedule'] = route
            yield train_item

            for item in data_list:
                time_table_item['train_num'] = train_item['train_num']
                time_table_item['serial_num'] = item['station_no']
                time_table_item['station_name'] = item['station_name']

                if item['arrive_time'] == '----':
                    time_table_item['time_arrive'] = item['start_time']
                else:
                    time_table_item['time_arrive'] = item['arrive_time']

                if item['start_time'] == '----':
                    time_table_item['time_arrive'] = '00:00:00'
                else:
                    time_table_item['time_depart'] = item['start_time']
                yield time_table_item











