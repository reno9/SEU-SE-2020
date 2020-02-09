import json
import re
import requests
import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def query(date,start,target):
    url = "https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date={0}&leftTicketDTO.from_station={1}&leftTicketDTO.to_station={2}&purpose_codes=ADULT".format(date,start,target)
    headers = {
        "Referer":"https://www.12306.cn/index/",
        "Cookie":"tk=ZPFtmT5-3WWUnW2xr__LPRDHSANucQa3glnyhDYl6NQwet1t0; JSESSIONID=990604405D87DB04601661B0D21558B8; BIGipServerpool_passport=300745226.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_wfdc_flag=dc; BIGipServeropn=1559233034.24610.0000; BIGipServerportal=3151233290.16671.0000; BIGipServerotn=1005584906.24610.0000; RAIL_EXPIRATION=1581366725222; RAIL_DEVICEID=AFFA5uCOJszrQLFkTtu0nXsIm-ptV97ik1Qoo4h6nMSizu2J6h5Xaw_VmTABFJRfSNkN9SjIR-ebyt_kGSs1xZOpHjW71gpZHp0eWCOCZTemJlpkJS6z2l-P8cxJRB4bBEtK00ZpfXfQDuKdq6jHORtd1ngNHjc6; _jc_save_fromDate=2020-02-09; _jc_save_toDate=2020-02-09; _jc_save_fromStation=%u5F90%u5DDE%2CXCH; _jc_save_toStation=%u82CF%u5DDE%2CSZH",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
    }
    result = requests.get(url,headers=headers)
    return result.text


def station_info():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9141'
    r = requests.get(url)
    info = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    res = re.findall(info,r.text)
    station = dict(res)
    return station