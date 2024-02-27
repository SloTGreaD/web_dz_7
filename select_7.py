from sqlalchemy import func
from main import session, Student, Grade, Group, Subject

group_id = 1  
subject_id = 1  

grades_in_group_for_subject = session.query(
    Student.id,
    Student.name,
    Grade.grade
).join(Grade, Student.id == Grade.student_id)\
 .filter(Student.group_id == group_id, Grade.subject_id == subject_id)\
 .all()

for grade in grades_in_group_for_subject:
    print(grade)
