import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.service import get_list_data

timelessons_db = get_list_data('timelessons')

from db.connect import mycursor
from prettytable import PrettyTable

def get_list_timelessons():
    mycursor.execute(
    """
    SELECT id as "Mã môn học", name as "Tên môn học", number_of_periods as "Số tiết"
    FROM subjects
    """
)

    result = mycursor.fetchall()
    
    x = PrettyTable()
    x.title = 'TIMELESSONS'
    columns = [i[0] for i in mycursor.description]
    x.field_names = columns
    for row in result:
        x.add_row(row)
    return x

#print(get_list_timelessons())
