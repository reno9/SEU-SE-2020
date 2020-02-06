import datetime
import requests
import urllib.parse

dict_station = {}


def station_name():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
    resp = requests.get(url)
    if resp.status_code == 200:
        print('获取站点信息成功!')
        for each in resp.text.split('=')[1].split('@')[1:]:
            station = each.split('|')
            dict_station[station[1]] = station[2]
    else:
        print('获取站点信息失败!')


def left_ticket(from_s, date, list1=[]):
    global dict_station
    url = "https://kyfw.12306.cn/otn/czxx/query?"
    dict1 = {'train_start_date': date,
             'train_station_name': urllib.parse.quote(from_s, 'GBK'),
             'train_station_code': dict_station[from_s],
             'randCode': ''}
    resp = requests.get(url, params=dict1, verify=False)
    print(resp.url)
    data = resp.json()
    trans = data['data']['data']
    if resp.status_code == 200:
        print('爬取信息成功!')
        dict1 = {
            'id': '',
            'from_station': '',
            'to_station': '',
            'from_date': '',
            'from_time': '',
            'arrive_date': '',
            'arrive_time': '',

        }
        for each in trans:
            dict1['id'] = each['station_train_code']
            dict1['from_station'] = each['start_station_name']
            dict1['to_station'] = each['end_station_name']
            dict1['from_date'] = datetime.datetime.strptime(each['start_train_date'], "%Y%m%d").date()
            dict1['from_time'] = each['start_start_time']
            if (each['start_start_time'] > each['end_arrive_time']):
                dict1['arrive_date'] = datetime.datetime.strptime(each['start_train_date'],
                                                                  "%Y%m%d").date() + datetime.timedelta(days=1)
            else:
                dict1['arrive_date'] = datetime.datetime.strptime(each['start_train_date'], "%Y%m%d").date()
            dict1['arrive_time'] = each['end_arrive_time']
            info = (dict1['id'], dict1['from_station'], dict1['to_station'], dict1['from_date'], dict1['from_time'],
                    dict1['arrive_date'], dict1['arrive_time'])
            list1.append(info)

    else:
        print('获取余票信息失败！')

    return list1
