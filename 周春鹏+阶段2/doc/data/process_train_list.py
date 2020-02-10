import pymysql

with open("train_list.json", 'r', encoding="utf8") as f:

    text = f.read()
    train_dict = eval(text)
    new_dict = {}

    dictD = train_dict["2019-10-10"]["D"]
    for item in dictD:
        new_dict[item['station_train_code']] = item['train_no']
    dictT = train_dict["2019-10-10"]["T"]
    for item in dictT:
        new_dict[item['station_train_code']] = item['train_no']
    dictG = train_dict["2019-10-10"]["G"]
    for item in dictG:
        new_dict[item['station_train_code']] = item['train_no']
    dictC = train_dict["2019-10-10"]["C"]
    for item in dictC:
        new_dict[item['station_train_code']] = item['train_no']
    dictO = train_dict["2019-10-10"]["O"]
    for item in dictO:
        new_dict[item['station_train_code']] = item['train_no']
    dictK = train_dict["2019-10-10"]["K"]
    for item in dictK:
        new_dict[item['station_train_code']] = item['train_no']
    dictZ = train_dict["2019-10-10"]["Z"]
    for item in dictZ:
        new_dict[item['station_train_code']] = item['train_no']

    db = pymysql.connect( user="root", password="111", host="localhost", port=3306, database="TrainQuery" )
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `train_num_no` (`train_num` VARCHAR(8), `train_route` VARCHAR(32), `no` VARCHAR(16), PRIMARY KEY (`train_num`)) DEFAULT CHARSET=utf8;")

    for dict_key, dict_value in new_dict.items():
        dict_key = dict_key.replace(")", "").split("(")
        n_train_num = dict_key[0]
        n_train_route = dict_key[1]
        n_no = dict_value
        sql = "INSERT INTO train_num_no (train_num, train_route, no) VALUES ('{}', '{}', '{}')".format(n_train_num, n_train_route, n_no)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            print("error")

    db.close()





