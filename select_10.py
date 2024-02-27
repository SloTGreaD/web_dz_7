from sqlalchemy import func
from main import session, Student, Grade, Group, Subject
student_id = 1  
teacher_id = 1  

courses_for_student_by_teacher = session.query(
    Subject.id,
    Subject.name
).join(Grade, Subject.id == Grade.subject_id)\
 .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)\
 .group_by(Subject.id)\
 .all()

for course in courses_for_student_by_teacher:
    print(course)
