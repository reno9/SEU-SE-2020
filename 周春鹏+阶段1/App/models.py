from App.ext import db

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

class TrainLine(BaseModel):
    train_type = db.Column(db.String(8))
    train_num = db.Column(db.String(16), unique=True, primary_key=True)
    station_depart = db.Column(db.String(64))
    station_arrive = db.Column(db.String(64))
    station_schedule = db.Column(db.String(512))

class TrainTimeTable(BaseModel):
    train_num = db.Column(db.String(16), db.ForeignKey(TrainLine.train_num))
    serial_num = db.Column(db.Integer)
    station_name = db.Column(db.String(64))
    time_arrive = db.Column(db.Time)
    time_depart = db.Column(db.Time)
