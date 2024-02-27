
from sqlalchemy import func
from main import session, Student, Grade

top_students = session.query(
    Student.id,
    Student.name,
    func.avg(Grade.grade).label('average_grade')
).join(Grade, Student.id == Grade.student_id)\
 .group_by(Student.id)\
 .order_by(func.avg(Grade.grade).desc())\
 .limit(5)\
 .all()

for student in top_students:
    print(student)