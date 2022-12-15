import uvicorn
from fastapi import FastAPI
from typing import List
from models import *

from database_configs import get_db

if __name__ == "__main__":
    app = FastAPI()
    db, engine = get_db(
        user=,
        password=,
        db=,
        host=,
        port=,
    )


    @app.get('/get-favourite-courses/{student_id}')
    def get_device_signals(
            student_id: int,
    ) -> List[str]:
        favourite_courses = db.query(FavouriteCourses).filter_by(student_id=student_id).all()
        return [fvc.course.name for fvc in favourite_courses]


    uvicorn.run(app)
