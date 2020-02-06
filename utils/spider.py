"""
https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2020-02-03&leftTicketDTO.from_station=JNK&leftTicketDTO.to_station=HIK&purpose_codes=ADULT

https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2020-02-03&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT
"""
import json

import requests
import re
import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def city():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9050'
    r = requests.get(url, verify=False)  # 提取网页信息，不判断证书
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'  # 正则表达式提取中文以及大写英文字母
    result = re.findall(pattern, r.text)  # 进行所需要的信息的提取
    station = dict(result)  # 把所获信息设置为一一对应
    return station


def query(times,local,destination):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={0}&leftTicketDTO.from_station={1}&leftTicketDTO.to_station={2}&purpose_codes=ADULT".format(times,local,destination)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E7%A6%8F%E5%B7%9E,FZS&date=2020-02-03&flag=N,N,Y",
        "Cookie": "JSESSIONID=7CA6583032DA109401B420841241F61A; BIGipServerotn=1257243146.50210.0000; RAIL_EXPIRATION=1581064868029; RAIL_DEVICEID=WkcogFDlUkooPyr4QHodphMCri9lIlYsqVBNNurInzylFpW6ynwafwDqU08CSqtn_0CfVWroVVPIcJPdm_RoJgzsx_dHKVEK9WNfjTL3yG1G-Cdrdp8PBymFDD-H0UPIfXEXMGGvXizDnOLRL5soITYebdw56a_o; BIGipServerpool_passport=267190794.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromDate=2020-02-03; _jc_save_toDate=2020-02-03; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5317%u4EAC%2CBJP",
    }
    r = requests.get(url,headers=headers)
    return r.text


if __name__ == '__main__':
    find_result = query("HIK", "JNK")
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
        info = {"车次名称": train_no, "出发站": from_station_name, "终点站": to_station_name, "出发时间": start_time,
                "到达时间": arrive_time, "总耗时": time_fucked_up, "一等座": first_class_seat, "二等座": second_class_seat,
                "软卧": soft_sleep, "硬卧": hard_sleep, "硬座": hard_seat, "无座": no_seat}

        info_list.append(info)
    print(info_list)



