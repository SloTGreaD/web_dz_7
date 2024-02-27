from sqlalchemy import func
from main import session, Student, Grade, Group, Subject
group_id = 1  

students_in_group = session.query(
    Student.id,
    Student.name
).filter(Student.group_id == group_id)\
 .all()

for student in students_in_group:
    print(student)
