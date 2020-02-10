from app import *

db.drop_all()
db.create_all()
train1 = Train(id='G7376', from_station='苏州', to_station='常州', start_time='17:10:00', arrive_time='17:15:00',
               date='2020-1-21')
train2 = Train(id='G7196', from_station='苏州', to_station='常州', start_time='17:09:00', arrive_time='17:46:00',
               date='2020-1-21')
train2 = Train(id='G7913', from_station='苏州', to_station='常州', start_time='17:27:00', arrive_time='17:58:00',
               date='2020-1-21')
train3 = Train(id='G7021', from_station='苏州', to_station='无锡', start_time='17:27:00', arrive_time='17:42:00',
               date='2020-1-21')
train4 = Train(id='G7222', from_station='苏州', to_station='无锡', start_time='17:32:00', arrive_time='17:47:00',
               date='2020-1-21')
train5 = Train(id='D3042', from_station='苏州', to_station='无锡', start_time='17:37:00', arrive_time='17:53:00',
               date='2020-1-21')
train6 = Train(id='G7022', from_station='苏州', to_station='南京', start_time='17:11:00', arrive_time='18:11:00',
               date='2020-1-21')
train7 = Train(id='G7056', from_station='苏州', to_station='南京', start_time='17:27:00', arrive_time='18:41:00',
               date='2020-1-21')
train8 = Train(id='G7024', from_station='苏州', to_station='南京', start_time='18:10:00', arrive_time='19:29:00',
               date='2020-1-21')
train9 = Train(id='G1919', from_station='苏州', to_station='上海', start_time='17:16:00', arrive_time='17:40:00',
               date='2020-1-21')
train10 = Train(id='G7143', from_station='苏州', to_station='上海', start_time='17:19:00', arrive_time='17:52:00',
                date='2020-1-21')
train11 = Train(id='G1955', from_station='苏州', to_station='上海', start_time='17:12:00', arrive_time='17:45:00',
                date='2020-1-21')
db.session.add_all([train1, train2, train3, train4, train5, train6, train7, train8, train9, train10,train11])
db.session.commit()
