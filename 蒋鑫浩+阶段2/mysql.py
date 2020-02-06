import pymysql  # 导入 pymysql


def mysqltrain(trains=[]):
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root",
                         password="root", db="train12306", port=3306)
    cur = db.cursor()
    for train in trains:
        cur.execute("insert into trains values('%s','%s','%s','%s','%s','%s','%s')" % (
            train[0], train[1], train[2], train[3], train[4], train[5], train[6]))
        db.commit()
    print("导入数据成功")