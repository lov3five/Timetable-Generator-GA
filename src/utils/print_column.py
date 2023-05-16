import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prettytable import PrettyTable

def print_list_one_column(columns):
    x = PrettyTable()
    x.field_names = ["Tên cột"]
    # STT tăng dần từ 0 không lấy từ columns
    for i in range(len(columns)):
        x.add_row([columns[i]])
    print(x)
    