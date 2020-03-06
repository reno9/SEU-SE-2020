# coding: utf-8
from sqlalchemy import Column, Integer, String, Text
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class EnBaseInfo(db.Model):
    __tablename__ = 'en_base_info'

    en_id = db.Column(db.Integer, primary_key=True, info='企业ID')
    en_name = db.Column(db.String(100), nullable=False, info='企业名')
    en_manage_state = db.Column(db.String(30), nullable=False, info='经营状态')
    en_representative = db.Column(db.String(70), info='法定代表人')
    en_registered_capital = db.Column(db.String(30), info='注册资本')
    en_entablish_date = db.Column(db.String(30), info='成立日期')
    en_province = db.Column(db.String(30), info='所属省份')
    en_city = db.Column(db.String(30), info='所属城市')
    en_telephone = db.Column(db.String(30), info='企业电话')
    en_telephone_more = db.Column(db.String(100), info='更多电话')
    en_email = db.Column(db.String(100), info='企业邮箱')
    en_social_code = db.Column(db.String(30), info='统一社会信用代码')
    en_identification_num = db.Column(db.String(30), info='纳税人识别号')
    en_registrate_num = db.Column(db.String(30), info='注册号')
    en_organization_code = db.Column(db.String(30), info='组织机构代码')
    en_insured_num = db.Column(db.String(30), info='参保人数')
    en_type = db.Column(db.String(30), info='企业类型')
    en_industry = db.Column(db.String(50), info='所属行业')
    en_website = db.Column(db.String(100), info='企业网址')
    en_address = db.Column(db.String(200), info='企业地址')
    en_scope = db.Column(db.String, info='经营范围')



class EnterpriseEngineer(db.Model):
    __tablename__ = 'enterprise_engineer'

    en_id = db.Column(db.Integer, info='企业id')
    en_name = db.Column(db.String(100), nullable=False, info='企业名')
    engineer_id = db.Column(db.Integer, primary_key=True, info='工程师ID')
    engineer_name = db.Column(db.String(20), nullable=False, info='工程师姓名')
    patent_num = db.Column(db.Integer, nullable=False, info='专利数量')
    engineer_first_kind = db.Column(db.String(30), info='所属一类技术领域')
    engineer_second_kind = db.Column(db.String(30), info='所属二类领域')
    engineer_third_kind = db.Column(db.String(30), info='所属三类领域')



class EnterprisePatent(db.Model):
    __tablename__ = 'enterprise_patent'

    en_id = db.Column(db.Integer, info='企业id')
    pa_id = db.Column(db.Integer, primary_key=True, info='专利ID')
    pa_name = db.Column(db.String(100), info='专利名')
    pa_app_num = db.Column(db.String(50), info='申请号')
    pa_filing_date = db.Column(db.String(30), info='申请日')
    pa_public_num = db.Column(db.String(50), info='公开号')
    pa_public_date = db.Column(db.String(30), info='公开日')
    pa_applicant = db.Column(db.String(150), info='申请人')
    pa_address = db.Column(db.String(300), info='地址')
    pa_inventor = db.Column(db.String(150), info='发明人')
    pa_country_code = db.Column(db.String(20), info='国审代码')
    pa_abstract = db.Column(db.Text, info='摘要')
    pa_principal_claim = db.Column(db.Text, info='主权项')
    pa_main_kind_num = db.Column(db.String(50), info='主分类号')
    pa_kind_num = db.Column(db.String(300), info='专利分类号')
    pa_first_kind = db.Column(db.String(30), info='所属一类技术领域')
    pa_second_kind = db.Column(db.String(30), info='所属二类技术领域')
    pa_third_kind = db.Column(db.String(100), info='所属三类技术领域')

class Ipc(db.Model):
    __tablename__ = 'ipc'

    ipc_id = db.Column(db.String(15), primary_key=True, info='ipc分类号')
    ipc_content = db.Column(db.Text, nullable=False, info='ipc注释')
    ipc_content_vector = db.Column(db.Text, info='ipc对应的技术领域向量')
    ipc_to_field_id = db.Column(db.Integer, info='ipc分类对应的技术领域id')
    ipc_to_field_kind = db.Column(db.String(100), info='ipc对应的技术领域种类')



class PaAbstractVector(db.Model):
    __tablename__ = 'pa_abstract_vector'

    pa_id = db.Column(db.Integer, primary_key=True, info='专利id')
    pa_name = db.Column(db.String(100), nullable=False, info='专利名')
    pa_abstract = db.Column(db.Text, nullable=False, info='专利摘要')
    pa_abstract_vector = db.Column(db.Text, nullable=False, info='专利摘要文本')



class TechnicalField(db.Model):
    __tablename__ = 'technical_field'

    field_id = db.Column(db.Integer, primary_key=True, info='领域id')
    firstkind = db.Column(db.String(30), nullable=False, info='一类技术领域')
    secondkind = db.Column(db.String(30), nullable=False, info='二类技术领域')
    thirdkind = db.Column(db.String(100), nullable=False, info='三类技术领域')
    content = db.Column(db.String, nullable=False, info='技术领域内容')
    vector = db.Column(db.String, nullable=False, info='技术领域文本向量')