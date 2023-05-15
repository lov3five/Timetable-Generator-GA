import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.service import get_list_data

# (get_list_data_pretty_table('instructors'))
instructors_data = get_list_data('instructors')

def get_instructor_by_id(id):
    for instructor_tuple in instructors_data:
        instructor = {'id': instructor_tuple[0], 'name': instructor_tuple[1], 'sex': instructor_tuple[2], 'email': instructor_tuple[3], 'phone_number': instructor_tuple[4], 'address': instructor_tuple[5]}
        if instructor['id'] == int(id):
            return instructor

#print(get_instructor_by_id(2))

from db.connect import mycursor
from prettytable import PrettyTable

def get_list_instructors():
    mycursor.execute(
    """
SELECT r.id as "Mã phòng học", r.name as "Tên phòng học", r.capacity as "Sức chứa", r.`type` as "Loại phòng"
FROM rooms r 
    """
    )

    result = mycursor.fetchall()
    
    x = PrettyTable()
    x.title = 'ROOMS'
    columns = [i[0] for i in mycursor.description]
    x.field_names = columns
    for row in result:
        x.add_row(row)
    return x

print(get_list_instructors())

