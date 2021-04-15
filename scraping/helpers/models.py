from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base

DB_NAME = 'result_data.db'
engine = create_engine(f'sqlite:///{DB_NAME}', echo=True)

Base = declarative_base()

class Teachers(Base):
    __tablename__ = 'teacher'
    full_name = Column(String,unique=False,primary_key=True )
    company =Column(String,unique=False)


class Course(Base):
    __tablename__ = 'course'
    course_name = Column(String, nullable=False)
    course_id = Column(String,primary_key=True)
    course_url = Column(String)
    price = Column(String, unique=False)
    level = Column(String,unique=False)
    teachers = Column(String, unique=False)

metadata = Base.metadata

if __name__ == '__main__':
    metadata.create_all(engine)