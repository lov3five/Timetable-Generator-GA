import connect
from connect import mycursor
import random
 

def to_acronym(string):
    words = string.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym


def create_course(name, max_students, instructor_subject_id):
    try:
        sql = "INSERT INTO courses (name, max_students, instructor_subject_id) VALUES (%s, %s, %s)"
        val = (name, max_students, instructor_subject_id)
        mycursor.execute(sql, val)
    except Exception as e:
        print('Error: ' + str(e))
    connect.mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# def update_course_by_id(id, object):
#     name = object['name']
#     max_students = object['max_students']
#     subject_id = object['subject_id']
#     try:
#         sql = "UPDATE courses SET name = %s, max_students = %s, instructor_subject_id = %s, schedules_id = %s WHERE id = %s"
#         val = (name, max_students, instructor_subject_id, schedules_id, id)
#         mycursor.execute(sql, val)
#     except Exception as e:
#         print('Error: ' + str(e))
#     connect.mydb.commit()
#     print(mycursor.rowcount, "record(s) affected")

def delete_course_by_id(id):
    try:
        sql = "DELETE FROM courses WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
    except Exception as e:
        print('Error: ' + str(e))
    connect.mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

from instructors_subjects import instructors_subjects_data, get_subject_by_instructor_id
from subjects import get_subject_by_id
from instructors import instructors_data, get_instructor_by_id

list_max_student = [60, 80]

# Random max_student with 60% 60 and 40% 80

# for i in range(100):
#     random_max_student = random.choices(list_max_student, weights=(85, 15), k=1)[0]
#     print(random_max_student)
# Create data for courses with each instructor_id have a 20 courses
for instructor_tuple in instructors_data:
    print(instructor_tuple[0])
    instructor_subjects = get_subject_by_instructor_id(instructor_tuple[0])
    subject_data =  get_subject_by_id(instructor_subjects['subject_id'])
    instructor_data =  get_instructor_by_id(instructor_subjects['instructor_id'])
    for i in range(20):
        random_max_student = random.choices(list_max_student, weights=(85, 15), k=1)[0]
        course_name = 'LHP' + '_' + to_acronym(subject_data['name']) + '_' + to_acronym(instructor_data['name'])
        create_course(course_name, random_max_student, instructor_subjects['id'])


# for instructor_tuple in instructors_data:
#     for instructor_subject_tuple in instructors_subjects_data:
#         instructor_subject =  {'id': instructor_subject_tuple[0], 'instructor_id': instructor_subject_tuple[1], 'subject_id': instructor_subject_tuple[2]}
#         subject_data =  get_subject_by_id(instructor_subject['subject_id'])
#         instructor_data =  get_instructor_by_id(instructor_subject['instructor_id'])
#         for i in range(20):
#             course_name = 'LHP' + '_' + to_acronym(subject_data['name']) + '_' + to_acronym(instructor_data['name'])
#             create_course(course_name, random_max_student, instructor_subject['id'])
