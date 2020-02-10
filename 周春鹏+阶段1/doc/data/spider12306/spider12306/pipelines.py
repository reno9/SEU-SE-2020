# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class TrainLinePipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='111', db='TrainQuery', charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, train_item, spider):
        t_train_type = train_item.get("train_type", "N/A")
        t_train_num = train_item.get("train_num", "N/A")
        t_station_depart = train_item.get("station_depart", "N/A")
        t_station_arrive = train_item.get("station_arrive", "N/A")
        t_station_schedule = train_item.get("station_schedule", "N/A")

        sql = "INSERT INTO train_line (train_type, train_num, station_depart, station_arrive, station_schedule) VALUES ('{}','{}','{}','{}','{}')".format(t_train_type, t_train_num, t_station_depart, t_station_arrive, t_station_schedule)

        try:
            self.cur.execute(sql)
            self.conn.commit()
            return train_item
        except:
            print("train line error")
            self.conn.rollback()
            return train_item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()


class TimeTablePipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='111', db='TrainQuery', charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, time_table_item, spider):

        t_station_name = time_table_item.get("station_name")
        if t_station_name:
            t_train_num = time_table_item.get("train_num", "N/A")
            t_serial_num = time_table_item.get("serial_num", "00")
            t_time_arrive = time_table_item.get("time_arrive", "00:00:00")
            t_time_depart = time_table_item.get("time_depart", "00:00:00")

            sql = "INSERT INTO train_time_table (train_num, serial_num, station_name, time_arrive, time_depart) VALUES ('{}', '{}', '{}', '{}', '{}')".format(t_train_num, t_serial_num, t_station_name, t_time_arrive, t_time_depart)
            self.cur.execute(sql)
            self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()





