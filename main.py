from typing import Union
from fastapi import FastAPI
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
"""app= FastAPI()

@app.get("/")
def read_root():
    return{"message":"hello from koyeb"}"""





class Content(BaseModel):
    name: str
    description: str

class Subject(BaseModel):
    name: str
    level: int
    credit_units: int
    price: float
    description: str
    contents: List[Content]

class Student(BaseModel):
    first_name: str
    last_name: str
    birth_year: int
    phone: str
    address: str
    academic_record: List[Subject]

class StudentUpdate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    address: str

app = FastAPI()


students_db = []


@app.post("/students/", response_model=Student)
def create_student(student: Student):
    students_db.append(student)
    return student

@app.get("/students/", response_model=List[Student])
def get_students():
    return students_db

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    if student_id < 0 or student_id >= len(students_db):
        raise HTTPException(status_code=404, detail="Student not found")
    return students_db[student_id]

@app.get("/students/{student_id}/academic_record", response_model=List[Subject])
def get_academic_record(student_id: int):
    if student_id < 0 or student_id >= len(students_db):
        raise HTTPException(status_code=404, detail="Student not found")
    return students_db[student_id].academic_record

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student_update: StudentUpdate):
    if student_id < 0 or student_id >= len(students_db):
        raise HTTPException(status_code=404, detail="Student not found")
    student = students_db[student_id]
    student.first_name = student_update.first_name
    student.last_name = student_update.last_name
    student.phone = student_update.phone
    student.address = student_update.address
    return student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id < 0 or student_id >= len(students_db):
        raise HTTPException(status_code=404, detail="Student not found")
    students_db.pop(student_id)
    return {"message": "Student deleted"}