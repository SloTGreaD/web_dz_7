from sqlalchemy import func
from main import session, Student, Grade, Group 

subject_id = 1  # Пример ID предмета

average_grade_by_group = session.query(
    Group.id,
    Group.name,
    func.avg(Grade.grade).label('average_grade')
).join(Student, Group.id == Student.group_id)\
 .join(Grade, Student.id == Grade.student_id)\
 .filter(Grade.subject_id == subject_id)\
 .group_by(Group.id)\
 .all()

for group in average_grade_by_group:
    print(group)
