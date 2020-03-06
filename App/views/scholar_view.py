import time

from flask import Blueprint, json

from App.models.enterprise_model import EnBaseInfo
from App.models.scholar_model import EsTeacher, EsInstitution, TeacherPaper, Paper, TeacherPatent2, Patent

blue_scholar = Blueprint("scholar", __name__, url_prefix='/scholar')

@blue_scholar.route('/<int:id>/')
def scholar_homepage(id):
    start_time = time.time()
    Teacher = EsTeacher()
    Institution = EsInstitution()
    Teacher_paper = TeacherPaper()
    PaperModel = Paper()
    TeacherPatent = TeacherPatent2()
    PatentModel = Patent()
    EnterpriseInfo = EnBaseInfo()

    # 查找个人信息
    found_teacher = Teacher.query.filter_by(ID=id).first_or_404()
    found_institution = Institution.query.filter_by(ID=found_teacher.INSTITUTION_ID).first_or_404()

    name = found_teacher.NAME
    university = found_institution.SCHOOL_NAME
    institution = found_institution.NAME
    title = found_teacher.TITLE
    email = found_teacher.EMAIL
    homepage = found_teacher.HOMEPAGE

    #查找团队数据（Neo4j）
    team = None

    #查找论文数据
    paper_list = Teacher_paper.query.filter_by(teacher_id = id).all()
    paper_id_list = [paper.paper_id for paper in paper_list]
    paper_data = []
    for paper_id in paper_id_list:
        paper = PaperModel.query.filter_by(id=paper_id).first()
        if paper:
            paper_name = paper.name
            paper_org = paper.org
            paper_year = paper.year
            paper_cited_num = paper.cited_num
            paper_data.append(
                {
                    "paper_name": paper_name,
                    "paper_org": paper_org,
                    "paper_year": paper_year,
                    "paper_cited_num": paper_cited_num
                }
            )

    patent_list = TeacherPatent.query.filter_by(teacher_id=id).all()
    patent_id_list = [patent.patent_id for patent in patent_list]
    patent_data = []
    for patent_id in patent_id_list:
        patent = PatentModel.query.filter_by(id=patent_id).first()
        if patent:
            patent_title = patent.title
            patent_number = patent.publication_number
            patent_year = patent.publication_year
            patent_data.append(
                {
                    "patent_title": patent_title,
                    "patent_number": patent_number,
                    "patent_year": patent_year,
                }
            )

    en_id_recommend = [7064, 7065, 7085]
    ent_data_recommend = []
    for en_id in en_id_recommend:
        enterprise = EnterpriseInfo.query.filter_by(en_id=en_id).first()
        en_name = enterprise.en_name
        ent_data_recommend.append(
            {
                "en_id": en_id,
                "en_name": en_name,
            }
        )

    page_data ={
        "status": 200,
        "name": name,
        "university": university,
        "institution": institution,
        "title": title,
        "email": email,
        "homepage": homepage,
        "team": team,
        "paper": paper_data,
        "patent": patent_data,
        "en_recommend": ent_data_recommend,
    }

    time_spend = time.time()-start_time
    print(page_data)
    print(time_spend)

    return "success"