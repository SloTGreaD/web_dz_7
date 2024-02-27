from sqlalchemy import func
from main import session, Student, Grade, Group, Subject

teacher_id = 1  # Пример ID преподавателя

courses_by_teacher = session.query(
    Subject.id,
    Subject.name
).filter(Subject.teacher_id == teacher_id)\
 .all()

for course in courses_by_teacher:
    print(course)
