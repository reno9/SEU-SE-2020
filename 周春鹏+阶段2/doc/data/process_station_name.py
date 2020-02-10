import pymysql

with open("station_name.json", 'r', encoding="utf8") as f:
    text = f.read()
    text = text.replace("@", "").split('|')
    print(text)

db = pymysql.connect( user="root", password="111", host="localhost", port=3306, database="TrainQuery" )
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS `station_list` (`station_num` VARCHAR(4), `station_name` VARCHAR(16), PRIMARY KEY (`station_num`)) DEFAULT CHARSET=utf8;")


i = 1
j = 2
while i < len(text) and j < len(text):
    print(text[j], text[i])
    sql = "INSERT INTO station_list (station_num, station_name) VALUES ('{}', '{}')".format(text[j], text[i])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("error")
    i = i + 5
    j = j + 5

db.close()

