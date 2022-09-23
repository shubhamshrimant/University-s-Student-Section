# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:21:59 2022

@author: shubh
"""

from .models import db
from .models import Students,Syllabuses,Courses

def get_all(model):
    data = db.session.query(model).all()
    return data

def get_by_enrollment_number(id):
    #data = db.session.query(model).filter(model.enrollment_number==id)
    
    data = db.session.query(Students,Syllabuses,Courses).filter(
        Students.course_id == Courses.id
        ).filter(
            Students.syllabus_id == Syllabuses.syllabus_id).filter(
    Students.enrollment_number == id
)
    return data

def get_by_courses_id(id):
    data = db.session.query(Students,Syllabuses,Courses).filter(
        Students.course_id == Courses.id
        ).filter(
            Students.syllabus_id == Syllabuses.syllabus_id).filter(
    Courses.id == id
).all()
    return data

def get_by_syllabuses_id(id):
    data = db.session.query(Students,Syllabuses,Courses).filter(
        Students.course_id == Courses.id
        ).filter(
            Students.syllabus_id == Syllabuses.syllabus_id).filter(
    Syllabuses.syllabus_id == id
).all()
    return data

def add_instance(model, **kwargs):
    try:
        instance = model(**kwargs)
        db.session.add(instance)
        commit_changes()
        msg = "Added successfully"
        return msg
    except:
        msg = "Can't add, check if the record already exists."
        return msg


def delete_instance(model, id):
    if model == Students:
        try:
            db.session.query(model).filter_by(enrollment_number=id).delete()
            commit_changes()
            msg = "Successfully deleted"
            return msg
        except:
            msg = "Cannot make the changes as the Courses/Syllabuses are used by Student"
            return msg
    elif model == Courses:
        try:
            
            db.session.query(model).filter_by(id=id).delete()
            msg = "Successfully deleted"
            
            return msg
        except:
            msg = "Cannot make the changes as the Courses/Syllabuses are used by Student"
            return msg
    elif model == Syllabuses:
        try:
            
            db.session.query(model).filter_by(syllabus_id=id).delete()
            commit_changes()
            msg = "Successfully deleted"
            return msg
        except:
            msg = "Cannot make the changes as the Courses/Syllabuses are used by Student"
            return msg
    


def edit_instance(model, id, **kwargs):
    if model == Students:
        instance = db.session.query(model).filter_by(enrollment_number=id).all()[0]
    elif model == Courses:
        instance = db.session.query(model).filter_by(id=id).all()[0]
    elif model == Syllabuses:
        instance = db.session.query(model).filter_by(syllabus_id=id).all()[0]
    #instance = db.session.query(model).filter_by(id=id).all()[0]
    for attr, new_value in kwargs.items():
        try:
            setattr(instance, attr, new_value)
            commit_changes()
            msg = "Successfully edited"
            return msg
        except:
             msg = "Cannot make the changes as the Courses/Syllabuses are used by Student"
             return msg
    


def commit_changes():
    db.session.commit()
