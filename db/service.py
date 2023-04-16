from prettytable import PrettyTable

from connect import mycursor

# TABLE COURSES
def get_list_data(name_table):
    mycursor.execute("SELECT * FROM {}".format(name_table))
    myresult = mycursor.fetchall()
    if myresult == []:
        print(name_table + ' no data!!!')
        return
    pretty_table(name_table, mycursor, myresult)
    return myresult
    
def pretty_table(name_table, cursor, result):
    """In ra bảng dữ liệu với định dạng đẹp.

    Hàm này sử dụng thư viện `prettytable` để in ra bảng dữ liệu với định dạng đẹp.

    Args:
        name_table (str): Tên của bảng cần in ra.
        cursor (Cursor): Đối tượng `Cursor` của `MySQLdb`.

    """
    # Tạo đối tượng PrettyTable
    x = PrettyTable()
    
    # Tiêu đề bảng
    x.title = name_table.upper()

    # Thiết lập các cột cho bảng
    columns = [i[0] for i in cursor.description]
    x.field_names = columns

    myresult = result
    # Thêm từng bản ghi vào bảng
    for row in myresult:
        x.add_row(row)

    # In bảng với định dạng đẹp của PrettyTable
    print(x)


