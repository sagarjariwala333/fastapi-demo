from sqlalchemy import Column, Integer, String # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    employee_id = Column(Integer)
