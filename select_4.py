from sqlalchemy import func
from main import session, Student, Grade, Group 
stream_average_grade = session.query(
    func.avg(Grade.grade).label('stream_average_grade')
).scalar()

print(stream_average_grade)
