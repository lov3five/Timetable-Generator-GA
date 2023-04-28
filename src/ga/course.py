import os
import sys
# Thêm đường dẫn vào `sys.path`
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db import courses_db

class Course:
    def __init__(self, course_id, course_name, max_students, instructor_id, instructor_name, subject_id, subject_name):
        self.course_id = course_id
        self.course_name = course_name
        self.max_students = max_students
        self.instructor_id = instructor_id
        self.instructor_name = instructor_name
        self.subject_id = subject_id
        self.subject_name = subject_name
        
    def get_course_id(self):
        return self.course_id
    
    def set_course_id(self, course_id):
        self.course_id = course_id
    
    def get_course_name(self):
        return self.course_name
    
    def set_course_name(self, course_name):
        self.course_name = course_name
    
    def get_max_students(self):
        return self.max_students
    
    def set_max_students(self, max_students):
        self.max_students = max_students
    
    def get_instructor_id(self):
        return self.instructor_id
    
    def set_instructor_id(self, instructor_id):
        self.instructor_id = instructor_id
    
    def get_instructor_name(self):
        return self.instructor_name
    
    def set_instructor_name(self, instructor_name):
        self.instructor_name = instructor_name
        
    def get_subject_id(self):
        return self.subject_id
    
    def set_subject_id(self, subject_id):
        self.subject_id = subject_id
    
    def get_subject_name(self):
        return self.subject_name
    
    def set_subject_name(self, subject_name):
        self.subject_name = subject_name
    
    def __str__(self):
        return f"Course: {self.course_id} | {self.course_name} | {self.max_students} | {self.instructor_id} | {self.instructor_name} | {self.subject_id} | {self.subject_name}"


# Hàm khởi tạo danh sách các khóa học
def init_courses(courses_db):
    courses = []
    for course in courses_db:
        courses.append(Course(course[0], course[1], course[2], course[3], course[4], course[5], course[6]))
    return courses
