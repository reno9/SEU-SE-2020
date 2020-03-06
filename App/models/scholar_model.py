# coding: utf-8
from sqlalchemy import Column, Integer, String, Text
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class EsDiscipline(db.Model):
    __tablename__ = 'es_discipline'

    CODE = db.Column(db.String(11), primary_key=True, info='学科代码')
    NAME = db.Column(db.String(128), info='学科名称')
    ROOT = db.Column(db.String(11), info='上级学科')



class EsHonor(db.Model):
    __tablename__ = 'es_honor'

    ID = db.Column(db.Integer, primary_key=True)
    TEACHER_ID = db.Column(db.Integer, info='教师ID')
    HONOR = db.Column(db.String(255), info='荣誉描述')
    YEAR = db.Column(db.String(4), info='时间')
    TYPE = db.Column(db.String(255), info='荣誉类型')



class EsInstitution(db.Model):
    __tablename__ = 'es_institution'

    ID = db.Column(db.Integer, primary_key=True, info='学院ID')
    SCHOOL_ID = db.Column(db.Integer, nullable=False, index=True, info='学校ID')
    SCHOOL_NAME = db.Column(db.String(128), info='学校名称')
    NAME = db.Column(db.String(128), info='学院名称')
    DFC_NUM = db.Column(db.Integer, info='一流学科数量')
    NKD_NUM = db.Column(db.Integer, info='重点学科数量')
    SKL_NUM = db.Column(db.Integer, info='重点实验室数量')
    ACADEMICIAN_NUM = db.Column(db.Integer, info='院士数量')
    CJSP_NUM = db.Column(db.Integer, info='长江学者数量')
    OUTSTANDING_NUM = db.Column(db.Integer, info='杰出青年数量')
    TTP_NUM = db.Column(db.Integer, info='千人计划数量')
    TTTP_NUM = db.Column(db.Integer, info='万人计划数量')



class EsRelationInDi(db.Model):
    __tablename__ = 'es_relation_in_dis'

    ID = db.Column(db.Integer, primary_key=True, info='学院学科ID')
    INSTITUTION_ID = db.Column(db.Integer, nullable=False, info='学院ID')
    DISCIPLINE_CODE = db.Column(db.String(11), nullable=False, info='学科ID')
    DFC = db.Column(db.Integer, info='是否一流学科')
    NKD = db.Column(db.Integer, info='是否重点学科')
    EVALUATION = db.Column(db.String(8), info='学科评估')



class EsSchool(db.Model):
    __tablename__ = 'es_school'

    ID = db.Column(db.Integer, primary_key=True, info='学校ID')
    CODE = db.Column(db.String(32), info='院校代号')
    NAME = db.Column(db.String(128), info='校名')
    EN_NAME = db.Column(db.String(128), info='英文校名')
    PROVINCE = db.Column(db.String(128), info='省份')
    CITY = db.Column(db.String(128), info='所在城市')
    LEVEL = db.Column(db.String(128), info='学校级别')
    FCU = db.Column(db.Integer, info='一流大学')
    URL = db.Column(db.String(1024), info='学校主页')
    LOGO = db.Column(db.String(128), info='学校图标')
    YEAR = db.Column(db.Integer, info='建校时间')
    ABB = db.Column(db.String(128), info='简称')
    INTRODUCTION = db.Column(db.Text, info='简介')
    NKD_NUM = db.Column(db.Integer, info='重点学科数量')
    SKL_NUM = db.Column(db.Integer, info='重点实验室数量')



class EsTeacher(db.Model):
    __tablename__ = 'es_teacher'

    ID = db.Column(db.Integer, primary_key=True, info='教师ID')
    NAME = db.Column(db.String(128), nullable=False, index=True, info='教师姓名')
    TITLE = db.Column(db.String(32), info='教师职称')
    SEX = db.Column(db.String(32), info='教师性别')
    SCHOOL_ID = db.Column(db.Integer, index=True, info='所在学校')
    INSTITUTION_ID = db.Column(db.Integer, index=True, info='所在学院')
    EDUEXP = db.Column(db.Text, info='教育经历')
    WORKEXP = db.Column(db.Text, info='工作经历')
    PROEXP = db.Column(db.Text, info='项目经历')
    EMAIL = db.Column(db.String(128), info='邮箱')
    TEL = db.Column(db.String(32), info='电话')
    PIC = db.Column(db.String(128), info='教师照片')
    HOMEPAGE = db.Column(db.String(1024), info='教师主页')
    BIRTHYEAR = db.Column(db.String(4), info='出生年份')
    FIELDS = db.Column(db.String(1024), info='研究领域')
    TOPICS = db.Column(db.Text, info='主题标签')
    DISCIPLINE_ID = db.Column(db.String(11), info='所属学科')
    SCI_NUM = db.Column(db.Integer, info='SCI数量')



class Fund(db.Model):
    __tablename__ = 'funds'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), info='教师名')
    year = db.Column(db.String(32), info='申报年份')
    title = db.Column(db.String(64), info='基金名')
    belong = db.Column(db.String(64), info='审批部门')
    org = db.Column(db.String(64), info='申报单位')
    type = db.Column(db.String(64), info='类型')
    money = db.Column(db.String(32), info='资金')






class Paper(db.Model):
    __tablename__ = 'paper'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    org = db.Column(db.String(64))
    year = db.Column(db.String(16))
    cited_num = db.Column(db.Integer)



class Patent(db.Model):
    __tablename__ = 'patent'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    category_code = db.Column(db.String(32))
    publication_number = db.Column(db.String(64))
    publication_year = db.Column(db.String(8))
    applicant = db.Column(db.String(128))
    address = db.Column(db.String(128))
    inventor = db.Column(db.String(128))
    code = db.Column(db.String(16))
    page_number = db.Column(db.String(8))



class TeacherAge(db.Model):
    __tablename__ = 'teacher_age'

    ID = db.Column(db.Integer, primary_key=True)
    AGE = db.Column(db.Integer)
    DETAIL = db.Column(db.String(255))



class TeacherContact(db.Model):
    __tablename__ = 'teacher_contact'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(765))
    phone = db.Column(db.String(60))
    fox = db.Column(db.String(60))
    email = db.Column(db.String(150))
    text = db.Column(db.String)
    status = db.Column(db.Integer)



class TeacherFund(db.Model):
    __tablename__ = 'teacher_funds'

    teacher_id = db.Column(db.Integer, primary_key=True, nullable=False)
    funds_id = db.Column(db.Integer, primary_key=True, nullable=False)



class TeacherPaper(db.Model):
    __tablename__ = 'teacher_paper'

    teacher_id = db.Column(db.Integer, primary_key=True, nullable=False)
    paper_id = db.Column(db.Integer, primary_key=True, nullable=False)



'''class TeacherPatent(db.Model):
    __tablename__ = 'teacher_patent'

    teacher_id = db.Column(db.Integer, primary_key=True, nullable=False)
    patent_code = db.Column(db.String(32), primary_key=True, nullable=False, info='专利号')'''



class TeacherPatent2(db.Model):
    __tablename__ = 'teacher_patent2'

    teacher_id = db.Column(db.Integer, primary_key=True, nullable=False)
    patent_id = db.Column(db.Integer, primary_key=True, nullable=False, info='专利id')



class TeacherdataInfo(db.Model):
    __tablename__ = 'teacherdata_info'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(255), nullable=False)
    homepage = db.Column(db.String(255))
    school = db.Column(db.String(32))
    institution = db.Column(db.String(32))
    info = db.Column(db.String)
    age = db.Column(db.Integer)
    position = db.Column(db.String(255))
    overseas_exp = db.Column(db.String(255))
    title = db.Column(db.String(255))
    fields = db.Column(db.String(512))
    eduexp = db.Column(db.Text)
    email = db.Column(db.Text)
    pic = db.Column(db.String(255))
    html = db.Column(db.String)
    age_description = db.Column(db.String(255))



