from sqlalchemy import func
from main import session, Student, Grade, Group, Subject
teacher_id = 1  

average_grade_by_teacher = session.query(
    func.avg(Grade.grade).label('teacher_average_grade')
).join(Subject, Grade.subject_id == Subject.id)\
 .filter(Subject.teacher_id == teacher_id)\
 .scalar()

print(average_grade_by_teacher)
