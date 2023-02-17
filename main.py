import random
import time


# Hàm Global
# Hàm xuất ra number phần tử ngẫu nhiên của list có thể trùng nhau
def random_elements_list(list, number):
    arr = []
    for i in range(0, number):
        arr.append(list[random.randint(0, len(list)-1)])
    return arr

# Hàm xuất ra number phần tử ngẫu nhiên của list không trùng nhau
def random_elements_no_duplicates(array, number):
    array_copy = array.copy()
    result = []
    for i in range(number):
        random_index = random.randint(0, len(array_copy) - 1)
        result.append(array_copy[random_index])
        array_copy.pop(random_index)
    return result

# Phòng học
class ClassRoom:
    def __init__(self, id, name, capacity, type):
        self._id = id
        self._name = name
        self._capacity = capacity
        self._type = type

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_capacity(self):
        return self._capacity

    def get_type(self):
        return self._type

    def __str__(self):
        return "Classroom: " + self._id + " | " + self._name + " | " + str(self._capacity) + " | " + self._type

# Giảng viên
class Instructor:
    def __init__(self, id, name, sex, email, phone, address):
        self._id = id
        self._name = name
        self._sex = sex
        self._email = email
        self._phone = phone
        self._address = address

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_sex(self):
        return self._sex

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone

    def get_address(self):
        return self._address

    def __str__(self):
        return "Instructor: " + self._id + " | " + self._name + " | " + str(self._sex) + " | " + self._email + " | " + self._phone + " | " + self._address

# Khoảng thời gian học (3 tiết/ca)
class TimeLessons:
    def __init__(self, id, time):
        self._id = id
        self._time = time

    def get_id(self):
        return self._id

    def get_time(self):
        return self._time

    def __str__(self):
        return "TimeLessons: " + self._id + " | " + self._time

# Lớp học phần(Khoá học)
class Course:
    def __init__(self, id, name, maxNumberOfStudents, instructors):
        self._id = id
        self._name = name
        self._maxNumberOfStudents = maxNumberOfStudents
        self._instructors = instructors

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_maxNumberOfStudents(self):
        return self._maxNumberOfStudents

    def get_instructors(self):
        return self._instructors

    def __str__(self):
        return "Course: " + self._id + " | " + self._name + " | " + str(self._maxNumberOfStudents) + " | " + str(self._instructors.get_name())

# Học phần(Môn học)
class Subject:
    def __init__(self, id, name, courses, numberOfCredits):
        self._id = id
        self._name = name
        self._courses = courses
        self._numberOfCredits = numberOfCredits

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_courses(self):
        return self._courses

    def get_numberOfCredits(self):
        return self._numberOfCredits

class Data:
    def __init__(self):
        self._rooms = []
        self._instructors = []
        self._timeLessons = []
        self._courses = []
        self._subjects = []
        self._numberCourseOfSubjects = 0

        # Load data input
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(ClassRoom(
                self.ROOMS[i][0], self.ROOMS[i][1], self.ROOMS[i][2], self.ROOMS[i][3]))

        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(
                self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1], self.INSTRUCTORS[i][2], self.INSTRUCTORS[i][3], self.INSTRUCTORS[i][4], self.INSTRUCTORS[i][5]))

        for i in range(0, len(self.TIMELESSONS)):
            self._timeLessons.append(TimeLessons(
                self.TIMELESSONS[i][0], self.TIMELESSONS[i][1]))

        for i in range(0, len(self.SUBJECT)):
            self._courses.append(Course(
                "L" + str(i+1), self.SUBJECT[i][0], 60, random_elements_list(self._instructors, 7)))

        for i in range(0, len(self.SUBJECT),3):
            self._subjects.append(Subject(
                "MHP" + str(i), self.SUBJECT[i][1], [self._courses[i],self._courses[i+1],self._courses[i+2]], 3))
        
        for i in range(0, len(self._subjects)):
            self._numberCourseOfSubjects += len(self._subjects[i].get_courses())

    SUBJECT = [
        ['TKHTAN1', 'Triển khai hệ thống an ninh'], ['TKHTAN2', 'Triển khai hệ thống an ninh'], ['TKHTAN3', 'Triển khai hệ thống an ninh'], ['CTDLVGT1', 'Cấu trúc dữ liệu và giải thuật'], ['CTDLVGT2', 'Cấu trúc dữ liệu và giải thuật'], ['CTDLVGT3', 'Cấu trúc dữ liệu và giải thuật'], ['ĐTVCM1', 'Định tuyến và chuyển mạch'], ['ĐTVCM2', 'Định tuyến và chuyển mạch'], ['ĐTVCM3', 'Định tuyến và chuyển mạch'], ['CNM1', 'Công nghệ mới'], ['CNM2', 'Công nghệ mới'], ['CNM3', 'Công nghệ mới'], ['LTĐT1', 'Lý thuyết đồ thị'], ['LTĐT2', 'Lý thuyết đồ thị'], ['LTĐT3', 'Lý thuyết đồ thị'], ['PTVTKHT1', 'Phân tích và thiết kế hệ thống'], ['PTVTKHT2', 'Phân tích và thiết kế hệ thống'], ['PTVTKHT3', 'Phân tích và thiết kế hệ thống'], ['TTNT1', 'Trí tuệ nhân tạo'], ['TTNT2', 'Trí tuệ nhân tạo'], ['TTNT3', 'Trí tuệ nhân tạo'], ['HCSDL1', 'Hệ cơ sở dữ liệu'], ['HCSDL2', 'Hệ cơ sở dữ liệu'], ['HCSDL3', 'Hệ cơ sở dữ liệu'], ['HTVCNW1', 'Hệ thống và công nghệ web'], ['HTVCNW2', 'Hệ thống và công nghệ web'], ['HTVCNW3', 'Hệ thống và công nghệ web'], ['KTLT1', 'Kỹ thuật lập trình'], [
            'KTLT2', 'Kỹ thuật lập trình'], ['KTLT3', 'Kỹ thuật lập trình'], ['XĐYCHT1', 'Xác định yêu cầu hệ thống'], ['XĐYCHT2', 'Xác định yêu cầu hệ thống'], ['XĐYCHT3', 'Xác định yêu cầu hệ thống'], ['MMT1', 'Mạng máy tính'], ['MMT2', 'Mạng máy tính'], ['MMT3', 'Mạng máy tính'], ['CTRR1', 'Cấu trúc rời rạc'], ['CTRR2', 'Cấu trúc rời rạc'], ['CTRR3', 'Cấu trúc rời rạc'], ['KTMT1', 'Kiến trúc máy tính'], ['KTMT2', 'Kiến trúc máy tính'], ['KTMT3', 'Kiến trúc máy tính'], ['PPLNCKH1', 'Phương pháp luận nghiên cứu khoa học'], ['PPLNCKH2', 'Phương pháp luận nghiên cứu khoa học'], ['PPLNCKH3', 'Phương pháp luận nghiên cứu khoa học'], ['LTHĐT1', 'Lập trình hướng đối tượng'], ['LTHĐT2', 'Lập trình hướng đối tượng'], ['LTHĐT3', 'Lập trình hướng đối tượng'], ['TCC21', 'Toán cao cấp 2'], ['TCC22', 'Toán cao cấp 2'], ['TCC23', 'Toán cao cấp 2'], ['LH1', 'Logic học'], ['LH2', 'Logic học'], ['LH3', 'Logic học'], ['VLĐC1', 'Vật lí đại cương'], ['VLĐC2', 'Vật lí đại cương'], ['VLĐC3', 'Vật lí đại cương'], ['TTDN1', 'Thực tập doanh nghiệp'], ['TTDN2', 'Thực tập doanh nghiệp'], ['TTDN3', 'Thực tập doanh nghiệp']
    ]

    ROOMS = [
        ["P1", "A1.01", 60, "Lý thuyết"],
        ["P2", "A2.01", 61, "Lý thuyết"],
        ["P3", "A3.01", 62, "Thực hành"],
        ["P4", "A4.01", 63, "Thực hành"],
        ["P5", "A5.01", 64, "Lý thuyết"],
        ["P6", "A6.01", 65, "Lý thuyết"],
        ["P7", "A7.01", 66, "Thực hành"],
        ["P8", "A8.01", 67, "Thực hành"],
        ["P9", "A9.01", 68, "Lý thuyết"],
        ["P10", "A10.01", 69, "Lý thuyết"],
        ["P11", "A11.01", 70, "Thực hành"],
        ["P12", "A12.01", 71, "Thực hành"],
        ["P13", "A13.01", 72, "Lý thuyết"],
        ["P14", "A14.01", 73, "Lý thuyết"],
        ["P15", "A15.01", 74, "Thực hành"],
        ["P16", "A16.01", 75, "Thực hành"],
        ["P17", "A17.01", 76, "Lý thuyết"],
        ["P18", "A18.01", 77, "Lý thuyết"],
        ["P19", "A19.01", 78, "Thực hành"],
        ["P20", "A20.01", 79, "Thực hành"]
    ]

    INSTRUCTORS = [
        ["GV1", "Nguyễn Thị Thảo", "Nữ", "nguyenthithao@gmail.com",
            "0956446246",  "303 Phạm Văn Đồng"],
        ["GV2", "Trần Văn Tài", "Nam", "tvantai@gmail.com",
            "0963847221",  "404 Trần Đại Nghĩa"],
        ["GV3", "Nguyễn Văn An", "Nam", "nguyenvanan@gmail.com",
            "0976488312",  "505 Nguyễn Văn Cừ"],
        ["GV4", "Phạm Thị Hoa", "Nữ", "phamthihoa@gmail.com",
            "0968597831",  "606 Trần Hưng Đạo"],
        ["GV5", "Đinh Văn Trường", "Nam", "dinhvantruong@gmail.com",
            "0935724661",  "707 Nguyễn Văn Trỗi"],
        ["GV6", "Lê Thị Hải", "Nữ", "lethihai@gmail.com",
            "0954378162",  "808 Trần Quốc Toản"],
        ["GV7", "Phạm Văn Hiếu", "Nam", "phamvanhieu@gmail.com",
            "0985461231",  "909 Nguyễn Văn Hữu"],
        ["GV8", "Nguyễn Thị Hạnh", "Nữ", "nguyenthihanh@gmail.com",
            "0956789432",  "1010 Nguyễn Trãi"],
        ["GV9", "Trần Văn Tuấn", "Nam", "tvantuan@gmail.com",
            "0987412587",  "1111 Trần Đại Nghĩa"],
        ["GV10", "Đặng Văn Tùng", "Nam", "dangvantung@gmail.com",
            "0956837452",  "1212 Trần Hưng Đạo"],
        ["GV11", "Phạm Thị Lộc", "Nữ", "phamthiloc@gmail.com",
            "0957642913",  "1313 Nguyễn Văn Cừ"],
        ["GV12", "Trần Văn Đạt", "Nam", "tvantdat@gmail.com",
            "0968273951",  "1414 Trần Đại Nghĩa"],
        ["GV13", "Lê Thị Mỹ", "Nữ", "lethimy@gmail.com",
            "0975836412",  "1515 Nguyễn Văn Trỗi"],
        ["GV14", "Nguyễn Văn Long", "Nam", "nguyenvanlong@gmail.com",
            "0964125739",  "1616 Trần Quốc Toản"],
        ["GV15", "Hoàng Thị Nga", "Nữ", "hoangthinga@gmail.com",
            "0953781926",  "1717 Nguyễn Văn Hữu"]
    ]

    TIMELESSONS = [["TG1", "Thứ Hai 06:30 - 09:00"],
                   ["TG2", "Thứ Hai 09:00 - 11:30"],
                   ["TG3", "Thứ Hai 12:30 - 15:00"],
                   ["TG4", "Thứ Hai 15:00 - 17:30"],
                   ["TG5", "Thứ Ba 06:30 - 09:00"],
                   ["TG6", "Thứ Ba 09:00 - 11:30"],
                   ["TG7", "Thứ Ba 12:30 - 15:00"],
                   ["TG8", "Thứ Ba 15:00 - 17:30"],
                   ["TG9", "Thứ Tư 06:30 - 09:00"],
                   ["TG10", "Thứ Tư 09:00 - 11:30"],
                   ["TG11", "Thứ Tư 12:30 - 15:00"],
                   ["TG12", "Thứ Tư 15:00 - 17:30"],
                   ["TG13", "Thứ Năm 06:30 - 09:00"],
                   ["TG14", "Thứ Năm 09:00 - 11:30"],
                   ["TG15", "Thứ Năm 12:30 - 15:00"],
                   ["TG16", "Thứ Năm 15:00 - 17:30"],
                   ["TG17", "Thứ Sáu 06:30 - 09:00"],
                   ["TG18", "Thứ Sáu 09:00 - 11:30"],
                   ["TG19", "Thứ Sáu 12:30 - 15:00"],
                   ["TG20", "Thứ Sáu 15:00 - 17:30"],
                   ["TG21", "Thứ Bảy 06:30 - 09:00"],
                   ["TG22", "Thứ Bảy 09:00 - 11:30"],
                   ["TG23", "Thứ Bảy 12:30 - 15:00"],
                   ["TG24", "Thứ Bảy 15:00 - 17:30"],
                   ["TG25", "Chủ Nhật 06:30 - 09:00"],
                   ["TG26", "Chủ Nhật 09:00 - 11:30"],
                   ["TG27", "Chủ Nhật 12:30 - 15:00"],
                   ["TG28", "Chủ Nhật 15:00 - 17:30"]]
    
    
    def get_rooms(self):
        return self._rooms
        
    def get_instructors(self):
        return self._instructors

    def get_number_of_periods(self):
        return self._timeLessons

    def get_courses(self):
        return self._courses

    def get_subjects(self):
        return self._subjects

    def get_number_course_of_subject(self):
        return self._numberCourseOfSubjects

class Display:
    def __init__(self,data):
        self._data = data

    def print_all_data(self):
        self.print_subjects()
    def print_subjects(self):
        subjects = self._data.get_subjects()
        print("Danh sách các môn học:")
        for subject in subjects:
            print(subject._name)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Hàm tạo lịch học
def create_schedule(population_size, lecturers, classrooms, periods):
    schedule = [ScheduleEntity(random.choice(lecturers), random.choice(
        classrooms), random.choice(periods)) for i in range(population_size)]
    return schedule

# Hàm đột biến
def mutate_entity(entity):
    entity.lecturer = random.choice(lecturers)
    entity.classroom = random.choice(classrooms)
    entity.number_of_periods = random.choice(periods)
    return entity

def main():
    data = Data()
    display = Display(data)
    display.print_all_data()
    # xác định dân số ban đầu của quần thể
    population_size = 100
    # xác định số thế hệ (lần lặp lại) thuật toán
    num_generations = 1000

    best_schedule = None
    best_fitness = 0
    start_time = time.time()

    end_time = time.time()

if __name__ == "__main__":
    main()

