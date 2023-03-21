import random

from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_rows([["Adelaide", 1295, 1158259, 600.5],
["Adelaide", 1295, 1158259, 600.5]])
print(x)
subjects = ["Triển khai hệ thống an ninh",
"Cấu trúc dữ liệu và giải thuật",
"Định tuyến và chuyển mạch",
"Công nghệ mới",
"Lý thuyết đồ thị",
"Phân tích và thiết kế hệ thống",
"Trí tuệ nhân tạo",
"Hệ cơ sở dữ liệu",
"Hệ thống và công nghệ web",
"Kỹ thuật lập trình",
"Xác định yêu cầu hệ thống",
"Mạng máy tính",
"Cấu trúc rời rạc",
"Kiến trúc máy tính",
"Phương pháp luận nghiên cứu khoa học",
"Lập trình hướng đối tượng",
"Toán cao cấp 2",
"Logic học",
"Vật lí đại cương",
"Thực tập doanh nghiệp"
]


def create_ma_monhoc(subjects):
    array = []
    for i, subject in enumerate(subjects):
        acronym = ""
        words = subject.split()
        for word in words:
            acronym += word[0]
        acronym = acronym.upper()
        for j in range(1, 4):
            array.append([acronym + str(j), subject])

    print(array)


def random_elements_no_duplicates(array, number):
    array_copy = array.copy()
    result = []
    for i in range(number):
        random_index = random.randint(0, len(array_copy) - 1)
        result.append(array_copy[random_index])
        array_copy.pop(random_index)
    return result

my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = random_elements_no_duplicates(my_array, 10)
print(result)

# Chọn ngẫu nhiên giáo viên phụ trách

intructors = ['GV1','GV2','GV3']
random.sample(intructors, random.randint(1, 3))