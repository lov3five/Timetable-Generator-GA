import os
import sys
from db import connect
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db.connect import mycursor
from db.service import get_list_data, pretty_table

def add_new_schedule(fitness):
    
    try:
        sql = "INSERT INTO schedules (fitness) VALUES (%s)"
        val = (fitness,)
        mycursor.execute(sql, val)
    except Exception as e:
        print('Error: ' + str(e))
    connect.mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    
def get_schedule_id_newest():
    try:
        sql = "SELECT id FROM schedules ORDER BY id DESC LIMIT 1"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return result[0]
    except Exception as e:
        print('Error: ' + str(e))