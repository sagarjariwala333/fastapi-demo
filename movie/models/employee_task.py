from sqlalchemy import Column, Integer, String, ForeignKey # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import relationship
from .employee import Employee
from .task import Task

Base = declarative_base()

class EmployeeTask(Base):
    __tablename__ = "employee_task"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey(Employee.id))
    task_id = Column(Integer, ForeignKey(Task.id))
