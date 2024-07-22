from sqlalchemy import Column, Integer, String, ForeignKey # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import relationship

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    
    employee = relationship("Employee", back_populates="tasks")