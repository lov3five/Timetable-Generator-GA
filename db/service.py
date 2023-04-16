from prettytable import PrettyTable

from connect import mycursor

# TABLE COURSES
def get_list_data_pretty_table(name_table):
    mycursor.execute("SELECT * FROM {}".format(name_table))
    myresult = mycursor.fetchall()
    if myresult == []:
        print(name_table + ' no data!!!')
        return

    # Tạo đối tượng PrettyTable
    x = PrettyTable()
    
    # Tiêu đề bảng
    x.title = name_table.upper()

    # Thiết lập các cột cho bảng
    columns = [i[0] for i in mycursor.description]
    x.field_names = columns

    # Thêm từng bản ghi vào bảng
    for row in myresult:
        x.add_row(row)

    # In bảng với định dạng đẹp của PrettyTable
    print(x)



def get_list_data(name_table):
    """Lấy dữ liệu từ một bảng trong cơ sở dữ liệu.

    Hàm này sử dụng một truy vấn SQL để lấy tất cả dữ liệu từ bảng có tên được cung cấp. Kết quả trả về được trả về dưới dạng danh sách các bản ghi, mỗi bản ghi là một tuple chứa các giá trị tương ứng với các cột trong bảng.

    Args:
        name_table (str): Tên của bảng cần lấy dữ liệu.

    Returns:
        list or None: Danh sách các bản ghi tương ứng với bảng được cung cấp. Nếu không có bản ghi nào được tìm thấy, hàm sẽ in ra thông báo và trả về `None`.

    """
    mycursor.execute("SELECT * FROM {}".format(name_table))
    myresult = mycursor.fetchall()
    if myresult == []:
        print(name_table + ' no data!!!')
        return

    return myresult

def to_acronym(string):
    words = string.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym
