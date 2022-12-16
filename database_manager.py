from database_configs import get_db
from models import *

if __name__ == "__main__":
    db, engine = get_db(
        user='testuser',
        password='password',
        db='software_db',
        host='localhost',
        port=5432,
    )

    Base.metadata.drop_all(
        bind=engine,
    )

    Base.metadata.create_all(bind=engine)

    std1 = Student(
        email='alireza@gmail.com'
    )
    db.add(std1)
    db.commit()

    std2 = Student(
        email='majid@gmail.com'
    )
    db.add(std2)
    db.commit()

    std3 = Student(
        email='arman@gmail.com'
    )
    db.add(std3)
    db.commit()

    crs1 = Course(
        name='cs1'
    )
    db.add(crs1)
    db.commit()

    crs2 = Course(
        name='cs2'
    )
    db.add(crs2)
    db.commit()

    crs3 = Course(
        name='cs3'
    )
    db.add(crs3)
    db.commit()

    fvc1 = FavouriteCourses(
        student_id=std1.id,
        course_id=crs1.id
    )
    db.add(fvc1)
    db.commit()

    fvc2 = FavouriteCourses(
        student_id=std1.id,
        course_id=crs2.id
    )
    db.add(fvc2)
    db.commit()

    fvc3 = FavouriteCourses(
        student_id=std1.id,
        course_id=crs3.id
    )
    db.add(fvc3)
    db.commit()

    fvc4 = FavouriteCourses(
        student_id=std2.id,
        course_id=crs1.id
    )
    db.add(fvc4)
    db.commit()

    fvc5 = FavouriteCourses(
        student_id=std2.id,
        course_id=crs3.id
    )
    db.add(fvc5)
    db.commit()

    fvc6 = FavouriteCourses(
        student_id=std3.id,
        course_id=crs2.id
    )
    db.add(fvc6)
    db.commit()
