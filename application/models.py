# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:18:16 2022

@author: shubh
"""

import flask_sqlalchemy
from sqlalchemy.orm import backref
db = flask_sqlalchemy.SQLAlchemy()


class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(100))
    
class Syllabuses(db.Model):
    __tablename__ = 'syllabuses'
    syllabus_id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(100))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    courses = db.relationship("Courses", backref=backref("courses", uselist=False))
    
class Students(db.Model):
    __tablename__ = 'students'
    enrollment_number = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    courses = db.relationship("Courses", backref=backref("courses", uselist=False))
    syllabus_id = db.Column(db.Integer, db.ForeignKey('syllabuses.syllabus_id'))
    courses = db.relationship("Syllabuses", backref=backref("syllabuses", uselist=False))
    