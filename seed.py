from faker import Faker
import random
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base, Student, Group, Teacher, Subject, Grade  
faker = Faker()

engine = create_engine('sqlite:///C:/Users/bayon/Desktop/web_dz_7/data/database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Створення груп
for _ in range(3):
    group = Group(name=faker.word())
    session.add(group)
session.commit()

# Створення викладачів
teachers = []
for _ in range(3):
    teacher = Teacher(fullname=faker.name())
    teachers.append(teacher)
    session.add(teacher)
session.commit()

# Створення предметів
subjects = []
for _ in range(5):
    subject = Subject(name=faker.word(), teacher=random.choice(teachers))
    subjects.append(subject)
    session.add(subject)
session.commit()

# Створення студентів і оцінок
groups = session.query(Group).all()
for _ in range(50):
    student = Student(fullname=faker.name(), group=random.choice(groups))
    session.add(student)
    session.commit()  

    for subject in subjects:
        for _ in range(random.randint(1, 20)): 
            grade = Grade(grade=random.randint(1, 10), date=faker.date_between(start_date='-1y', end_date='today'), student_id=student.id, subject_id=subject.id)
            session.add(grade)
session.commit()





