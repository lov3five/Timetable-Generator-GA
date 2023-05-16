import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prettytable import PrettyTable

def print_schedule(schedule):
    x = PrettyTable()
    x.title = 'Bảng lịch học tối ưu'
    x.field_names = ["Tên lớp học phần", "Tên lớp", "Tên môn học", "Tên phòng học", "Tên giảng viên", "Thời gian học"]
    for classes in schedule.get_classes():
        
    
    