from sqlalchemy import func, desc
from main import Session, Student, Grade  

def select_1():
    session = Session()
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    session.close()
    return result
