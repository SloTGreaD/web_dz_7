from sqlalchemy import func
from main import session, Student, Grade

subject_id = 1  # Пример ID предмета

top_student_for_subject = session.query(
    Student.id,
    Student.name,
    func.avg(Grade.grade).label('average_grade')
).join(Grade, Student.id == Grade.student_id)\
 .filter(Grade.subject_id == subject_id)\
 .group_by(Student.id)\
 .order_by(func.avg(Grade.grade).desc())\
 .first()

print(top_student_for_subject)
