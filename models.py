
from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        UniqueConstraint
                        )

from sqlalchemy.orm import relationship

from database_configs import Base


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer(), primary_key=True)
    email = Column(String(length=255), unique=True)


class Course(Base):
    __tablename__ = "course"
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=255), unique=True)


class FavouriteCourses(Base):
    __tablename__ = "favourite_courses"
    id = Column(Integer(), primary_key=True)
    student_id = Column(
        Integer(),
        ForeignKey("student.id"),
        nullable=False,
    )
    course_id = Column(
        Integer(),
        ForeignKey("course.id"),
        nullable=False,
    )
    student = relationship("Student")
    course = relationship("Course")
    __table_args__ = (
        UniqueConstraint("student_id", "course_id", name="student_course_unique_constraint"),
    )
