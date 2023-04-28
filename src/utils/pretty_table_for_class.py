import os
import sys

# Thêm đường dẫn vào `sys.path`
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prettytable import PrettyTable

# Hàm hiển thị danh sách của một lớp Class (Object)
def pretty_table_for_class(class_object):
    # Lấy ra tên của lớp Class
    class_name = class_object.__class__.__name__
    # Lấy ra danh sách các thuộc tính của lớp Class
    class_attributes = class_object.__dict__
    # Khởi tạo đối tượng PrettyTable
    table = PrettyTable()
    # Thêm tên của lớp Class vào danh sách các cột
    table.field_names = [class_name]
    # Thêm các thuộc tính của lớp Class vào danh sách các cột
    table.add_row(class_attributes.values())
    # Trả về đối tượng PrettyTable
    return table