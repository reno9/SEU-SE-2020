# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TrainLine(scrapy.Item):
    train_type = scrapy.Field()       #火车类型
    train_num = scrapy.Field()        #火车车次
    station_depart = scrapy.Field()   #始发站
    station_arrive = scrapy.Field()   #终点站
    station_schedule = scrapy.Field() #经过车站

class TimeTable(scrapy.Item):
    train_num = scrapy.Field()        #火车车次
    serial_num = scrapy.Field()       #车站序列号
    station_name = scrapy.Field()     #车站名
    time_arrive = scrapy.Field()      #到达时间
    time_depart = scrapy.Field()      #出发时间
