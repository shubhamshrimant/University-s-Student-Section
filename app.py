# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:20:24 2022

@author: shubh
"""

import json

from flask import request,jsonify

from application import create_app
from application import database
from application.models import Students,Syllabuses,Courses

app = create_app()

@app.route('/')
@app.route('/student', methods=['GET','POST','DELETE','PATCH'])
def student():
    if request.method == 'GET':
        students = database.get_all(Students)
        all_students = []
        for student in students:
            new_student = {
                "enrollment_number": student.enrollment_number,
                "course_id": student.course_id,
                "syllabus_id": student.syllabus_id
            }

            all_students.append(new_student)
            
        
        return jsonify(all_students)
    
    elif request.method == 'POST':
        data = request.get_json()
        enroll_id = data['enroll_id']
        syllabus_id = data['syllabus_id']
        course_id = data['course_id']
        #name = data['name']

        msg = database.add_instance(Students,enrollment_number=enroll_id, syllabus_id = syllabus_id, course_id=course_id)
        return msg
    
    elif request.method == 'DELETE':
        data = request.get_json()
        enroll_id = data['enroll_id']
        
        #name = data['name']

        msg = database.delete_instance(Students, id=enroll_id)
        return msg
    
    elif request.method == 'PATCH':
        data = request.get_json()
        enroll = data['enroll_id']
        new_course_id = data['new_course_id']
        msg = database.edit_instance(Students, id=enroll, course_id = new_course_id)
        return msg
        
        
    

@app.route('/course', methods=['GET','POST','DELETE','PATCH'])
def course():
    
    if request.method == 'GET':
        courses = database.get_all(Courses)
        all_courses = []
        for course in courses:
            new_course = {
                "enrollment_number": course.id
                
            }
    
            all_courses.append(new_course)
            
        return jsonify(all_courses)
    
    elif request.method == 'POST':
        data = request.get_json()
        #enroll = data['enroll']
        id = data['course_id']
        #name = data['name']

        msg = database.add_instance(Courses,id=id)
        return msg
    
    elif request.method == 'DELETE':
        data = request.get_json()
        id = data['id']
        
        #name = data['name']

        msg = database.delete_instance(Courses, id=id)
        return msg
    
    elif request.method == 'PATCH':
        data = request.get_json()
        old_course_id = data['old_course_id']
        new_course_id = data['new_course_id']
        msg = database.edit_instance(Courses, id=old_course_id, new_course_id=new_course_id)
        return msg
        

@app.route('/syllabus', methods=['GET','POST','DELETE','PATCH'])
def syllabus():
    if request.method == 'GET':
        syllabuses = database.get_all(Syllabuses)
        all_syllabuses = []
        for syllabus in syllabuses:
            new_syllabus = {
                
                "course_id": syllabus.course_id,
                "syllabus_id": syllabus.syllabus_id
            }

            all_syllabuses.append(new_syllabus)
            
        
        return jsonify(all_syllabuses)
    elif request.method == 'POST':
        data = request.get_json()
        #enroll = data['enroll']
        syllabus_id = data['syllabus_id']
        course_id = data['course_id']
        #name = data['name']

        msg =database.add_instance(Syllabuses,syllabus_id=syllabus_id, course_id=course_id)
        return msg
    
    elif request.method == 'DELETE':
        data = request.get_json()
        syllabus_id = data['syllabus_id']
        
        #name = data['name']

        msg = database.delete_instance(Syllabuses, id=syllabus_id)
        return msg
    
    elif request.method == 'PATCH':
        data = request.get_json()
        old_syllabus_id = data['old_syllabus_id']
        #new_course_id = data['course_id']
        new_syllabus_id = data['new_syllabus_id']
        msg = database.edit_instance(Syllabuses, id=old_syllabus_id, syllabus_id = new_syllabus_id)
        return msg
    
@app.route("/student_by_enrollment_id/<id>")
def students_by_enrollment(id):
    students = database.get_by_enrollment_number(id)
    all_students = []
    for student in students:
        new_student = {
            "enrollment_number": student.Students.enrollment_number,
            "course_id": student.Students.course_id,
            "syllabus_id": student.Students.syllabus_id
        }

        all_students.append(new_student)
        
    
    return jsonify(all_students)

        
@app.route("/student_by_course_id/<id>")
def students_by_course(id):
    students = database.get_by_courses_id(id)
    all_students = []
    for student in students:
        new_student = {
            "enrollment_number": student.Students.enrollment_number,
            "course_id": student.Courses.id,
            "syllabus_id": student.Syllabuses.syllabus_id
        }

        all_students.append(new_student)
        
    
    return jsonify(all_students)

@app.route("/student_by_syllabus_id/<id>")
def students_by_syllabus(id):
    students = database.get_by_syllabuses_id(id)
    all_students = []
    for student in students:
        new_student = {
            "enrollment_number": student.Students.enrollment_number,
            "course_id": student.Courses.id,
            "syllabus_id": student.Syllabuses.syllabus_id
        }

        all_students.append(new_student)
        
    
    return jsonify(all_students)

    

