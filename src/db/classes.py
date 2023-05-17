import os
import sys
from db import connect
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db.connect import mycursor

from db.service import get_list_data, pretty_table

def create_classes(course_id, room_id, timelesson_id, schedule_id):
    try:
        sql = "INSERT INTO classes (course_id, room_id, timelesson_id, schedule_id) VALUES (%s, %s, %s, %s, %s)"
        val = (id, course_id, room_id, timelesson_id, schedule_id)
        mycursor.execute(sql, val)
    except Exception as e:
        print('Error: ' + str(e))
    connect.mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    
def delete_all_classes():
    try:
        sql = "DELETE FROM classes"
        mycursor.execute(sql)
    except Exception as e:
        print('Error: ' + str(e))
    connect.mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
    
def get_list_classes_by_schedule_id(schedule_id):
    try:
        sql = "SELECT * FROM classes WHERE schedule_id = %s"
        val = (schedule_id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        return get_list_data(myresult, mycursor)
    except Exception as e:
        print('Error: ' + str(e))
        
def get_list_classes_by_classroom_id(classroom_id):
    try:
        sql = "SELECT * FROM classes WHERE classroom_id = %s"
        val = (classroom_id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        return get_list_data(myresult, mycursor)
    except Exception as e:
        print('Error: ' + str(e))