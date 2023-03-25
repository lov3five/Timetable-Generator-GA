import random
import time

from prettytable import PrettyTable

# note 
# 1 học kỳ 30 môn
# giảng viên 50 giảng viên
# Lớp học phần 3 lớp * 4 môn 
# làm thêm lớp khoa
# 50 giang viên 30 môn , 20 lớp

# 

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
class Room:
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
        return "Room: " + self._id + " | " + self._name + " | " + str(self._capacity) + " | " + self._type

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
        return "Course: " + self._id + " | " + self._name + " | " + str(self._maxNumberOfStudents) 

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

class Classes:
    def __init__(self,stt,subject,course):
        self._stt = stt
        self._subject = subject
        self._course = course
        self._room = None
        self._instructors = None
        self._time = None

    def get_stt(self):
        return self._stt
    def get_subject(self):
        return self._subject
    def get_course(self):
        return self._course
    def get_room(self):
        return self._room
    def get_instructors(self):
        return self._instructors
    def get_time(self):
        return self._time
    def set_room(self,room):
        self._room = room
    def set_instructors(self,instructors):
        self._instructors = instructors
    def set_time(self,time):
        self._time = time

    def __str__(self):
        return str(self._subject.get_id())+","+str(self._course.get_id())+","+str(self._room.get_id())+","+str(self._instructors.get_id())+","+str(self._time.get_id())

class Schedule:
    def __init__(self,data):
        self._data = data
        self._classes = []
        self._fitness = 0
        self._numberOfConflicts = 0
        self._idCLasses = 0
    
    # Create individual
    def create_schedule(self):
        for i in range(0,len(self._data.get_subjects())):
            for j in range(0,len(self._data.get_subjects()[i].get_courses())):
                newClasses = Classes(self._idCLasses,self._data.get_subjects()[i],self._data.get_subjects()[i].get_courses()[j])
                self._idCLasses += 1
                newClasses.set_room(random.choice(self._data.get_rooms()))
                newClasses.set_instructors(random.choice(self._data.get_subjects()[i].get_courses()[j].get_instructors()))
                newClasses.set_time(random.choice(self._data.get_time_lessons()))
                self._classes.append(newClasses)
        return self

    # Hàm tính độ thích nghi
    # def calculate_fitness(self):
    #     #self._numberOfConflicts = 0
    #     self._isFitnessChanged = True
    #     self._fitness = 0
    #     classes = self.get_classes()
    #     # for i in range(0,len(classes)):
    #     #     # Kiểm tra xem phòng có đủ chỗ không
    #     #     if(classes[i].get_room().get_capacity() < classes[i].get_course().get_maxNumberOfStudents()):
    #     #         self._numberOfConflicts += 1
    #     # return self._numberOfConflicts
    #     for i in range(0, len(classes)):
    #         for j in range(i+1, len(classes)):
    #             # cùng phòng 
    #             if(classes[i].get_room().get_id() == classes[j].get_room().get_id()):
    #                 # khác thời gian
    #                 """ Vì 2 lớp học phần cùng phòng học nhưng khác thời gian thì không bị trùng lịch => Không quan tâm đến giảng viên và môn học """
    #                 if(classes[i].get_time().get_id() != classes[j].get_time().get_id()):
    #                     self._fitness += 1
    #                 # cùng thời gian => trùng lịch
    #             # khác phòng
    #             else:
    #                 # cùng thời gian
    #                 if(classes[i].get_time().get_id() == classes[j].get_time().get_id()):
    #                     # khác giảng viên 
    #                     """ Vì khác giảng viên nên trùng môn học hay khác môn cũng không trùng lịch """
    #                     if(classes[i].get_instructors().get_id() != classes[j].get_instructors().get_id()):
    #                         self._fitness += 1
    #                     # cùng giảng viên => trùng lịch 
    #                 # khác thời gian 
    #                 else:
    #                     self._fitness += 1
    #     return self._fitness
    
    def calculate_fitness(self):
        self._numberOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            # Kiểm tra logic sức chứa phòng học và số lượng sinh viên
            if(classes[i].get_room().get_capacity() < classes[i].get_course().get_maxNumberOfStudents()):
                self._numberOfConflicts += 1
            for j in range(i+1, len(classes)):
                # Kiểm tra trùng lịch giảng dạy
                if(classes[i].get_instructors() == classes[j].get_instructors() and classes[i].get_time() == classes[j].get_time()):
                    self._numberOfConflicts += 1
                # Kiểm tra trùng lịch học
                if(classes[i].get_course() == classes[j].get_course() and classes[i].get_time() == classes[j].get_time()):
                    self._numberOfConflicts += 1
                # Kiểm tra trùng lịch giảng dạy và học
                if(classes[i].get_room() == classes[j].get_room() and classes[i].get_time() == classes[j].get_time()):
                    if(classes[i].get_course() != classes[j].get_course()):
                        self._numberOfConflicts += 1
        # Đảm bảo cho giá trị fitness luôn nằm trong khoảng từ 0-1
        return 1/(1.0*self._numberOfConflicts + 1)

    def get_fitness(self):
        if(self._isFitnessChanged == True):
            self._fitness = round(self.calculate_fitness(),3)
            self._isFitnessChanged = False
        return self._fitness

    def get_numberOfConflicts(self):
        return self._numberOfConflicts
    
    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes
    def __str__(self):
        value = ""
        for i in range(0,len(self._classes)):
            value += str(self._classes[i]) + ","
        value += str(self._classes[len(self._classes)-1])
        return value

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
            self._rooms.append(Room(
                self.ROOMS[i][0], self.ROOMS[i][1], self.ROOMS[i][2], self.ROOMS[i][3]))

        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(
                self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1], self.INSTRUCTORS[i][2], self.INSTRUCTORS[i][3], self.INSTRUCTORS[i][4], self.INSTRUCTORS[i][5]))

        for i in range(0, len(self.TIMELESSONS)):
            self._timeLessons.append(TimeLessons(
                self.TIMELESSONS[i][0], self.TIMELESSONS[i][1]))
        
        # Lớp học phần ( đưa vào lớp học, giảng viên)
        course1 = Course("LHP1", "Toán cao cấp - 15A", 60,[self._instructors[0],self._instructors[4],self._instructors[5],self._instructors[7],self._instructors[9],self._instructors[15],self._instructors[20],self._instructors[21],self._instructors[26]])
        course2 = Course("LHP2", "Toán cao cấp - 15B", 70, [self._instructors[0],self._instructors[4],self._instructors[5],self._instructors[7],self._instructors[9],self._instructors[15],self._instructors[20],self._instructors[21],self._instructors[26]])
        course3 = Course("LHP3", "Kỹ thuật lập trình - 15A",60, [self._instructors[0],self._instructors[2],self._instructors[5],self._instructors[7],self._instructors[10],self._instructors[15],self._instructors[20],self._instructors[22],self._instructors[26]])
        course4 = Course("LHP4", "Kỹ thuật lập trình - 15B", 70, [self._instructors[0],self._instructors[2],self._instructors[5],self._instructors[7],self._instructors[10],self._instructors[15],self._instructors[20],self._instructors[22],self._instructors[26]])
        course5 = Course("LHP5", "Kỹ thuật lập trình - 15C", 70, [self._instructors[0],self._instructors[2],self._instructors[5],self._instructors[7],self._instructors[10],self._instructors[15],self._instructors[20],self._instructors[22],self._instructors[26]])
        course6 = Course("LHP6", "Triển khai hệ thống an ninh - 15A", 70, [self._instructors[1],self._instructors[3],self._instructors[5],self._instructors[8],self._instructors[11],self._instructors[14],self._instructors[20],self._instructors[21],self._instructors[27]])
        course7 = Course("LHP7", "Triển khai hệ thống an ninh - 15B", 70, [self._instructors[1],self._instructors[3],self._instructors[5],self._instructors[8],self._instructors[11],self._instructors[14],self._instructors[20],self._instructors[21],self._instructors[27]])
        course8 = Course("LHP8", "Triển khai hệ thống an ninh - 15C", 70, [self._instructors[1],self._instructors[3],self._instructors[5],self._instructors[8],self._instructors[11],self._instructors[14],self._instructors[20],self._instructors[21],self._instructors[27]])
        course9 = Course("LHP9", "Cấu trúc dữ liệu và giải thuật - 15A", 65, [self._instructors[1],self._instructors[3],self._instructors[6],self._instructors[9],self._instructors[11],self._instructors[16],self._instructors[19],self._instructors[26],self._instructors[29]])
        course10 = Course("LHP10", "Cấu trúc dữ liệu và giải thuật - 15B", 65, [self._instructors[1],self._instructors[3],self._instructors[6],self._instructors[9],self._instructors[11],self._instructors[16],self._instructors[19],self._instructors[26],self._instructors[29]])
        course11 = Course("LHP11", "Cấu trúc dữ liệu và giải thuật - 15C", 65, [self._instructors[1],self._instructors[3],self._instructors[6],self._instructors[9],self._instructors[11],self._instructors[16],self._instructors[19],self._instructors[26],self._instructors[29]])
        course12 = Course("LHP12", "Định tuyến và chuyển mạch - 15A", 60, [self._instructors[4],self._instructors[7],self._instructors[8],self._instructors[9],self._instructors[12],self._instructors[18],self._instructors[23],self._instructors[28],self._instructors[30]])
        course13 = Course("LHP13", "Định tuyến và chuyển mạch - 15B", 60, [self._instructors[4],self._instructors[7],self._instructors[8],self._instructors[9],self._instructors[12],self._instructors[18],self._instructors[23],self._instructors[28],self._instructors[30]])
        course14 = Course("LHP14", "Định tuyến và chuyển mạch - 15C", 60,[self._instructors[4],self._instructors[7],self._instructors[8],self._instructors[9],self._instructors[12],self._instructors[18],self._instructors[23],self._instructors[28],self._instructors[30]])
        course15 = Course("LHP15", "Công nghệ mới - 15A", 80, [self._instructors[4],self._instructors[6],self._instructors[11],self._instructors[13],self._instructors[16],self._instructors[18],self._instructors[22],self._instructors[29],self._instructors[30]])
        course16 = Course("LHP16", "Công nghệ mới - 15B", 80, [self._instructors[4],self._instructors[6],self._instructors[11],self._instructors[13],self._instructors[16],self._instructors[18],self._instructors[22],self._instructors[29],self._instructors[30]])
        course17 = Course("LHP17", "Lý thuyết đồ thị - 15A", 70, [self._instructors[2],self._instructors[3],self._instructors[5],self._instructors[6],self._instructors[9],self._instructors[16],self._instructors[21],self._instructors[27],self._instructors[28]])
        course18 = Course("LHP18", "Lý thuyết đồ thị - 15B", 70, [self._instructors[2],self._instructors[3],self._instructors[5],self._instructors[6],self._instructors[9],self._instructors[16],self._instructors[21],self._instructors[27],self._instructors[28]])
        course19 = Course("LHP19", "Lý thuyết đồ thị - 15C", 70, [self._instructors[2],self._instructors[3],self._instructors[5],self._instructors[6],self._instructors[9],self._instructors[16],self._instructors[21],self._instructors[27],self._instructors[28]])
        course20 = Course("LHP20", "Phân tích và thiết kế hệ thống - 15A", 70, [self._instructors[2],self._instructors[4],self._instructors[7],self._instructors[8],self._instructors[11],self._instructors[17],self._instructors[18],self._instructors[28],self._instructors[30]])
        course21 = Course("LHP21", "Phân tích và thiết kế hệ thống - 15B", 70, [self._instructors[2],self._instructors[4],self._instructors[7],self._instructors[8],self._instructors[11],self._instructors[17],self._instructors[18],self._instructors[28],self._instructors[30]])
        course22 = Course("LHP22", "Trí tuệ nhân tạo - 15A", 80, [self._instructors[5],self._instructors[7],self._instructors[12],self._instructors[14],self._instructors[18],self._instructors[20],self._instructors[25],self._instructors[26],self._instructors[29]])
        course23 = Course("LHP23", "Trí tuệ nhân tạo - 15B", 80, [self._instructors[5],self._instructors[7],self._instructors[12],self._instructors[14],self._instructors[18],self._instructors[20],self._instructors[25],self._instructors[26],self._instructors[29]])
        course24 = Course("LHP24", "Hệ cơ sở dữ liệu - 15A", 70, [self._instructors[5],self._instructors[6],self._instructors[10],self._instructors[13],self._instructors[16],self._instructors[19],self._instructors[23],self._instructors[24],self._instructors[30]])
        course25 = Course("LHP25", "Hệ cơ sở dữ liệu - 15B", 70, [self._instructors[5],self._instructors[6],self._instructors[10],self._instructors[13],self._instructors[16],self._instructors[19],self._instructors[23],self._instructors[24],self._instructors[30]])
        course26 = Course("LHP26", "Hệ cơ sở dữ liệu - 15C", 70, [self._instructors[5],self._instructors[6],self._instructors[10],self._instructors[13],self._instructors[16],self._instructors[19],self._instructors[23],self._instructors[24],self._instructors[30]])
        course27 = Course("LHP27", "Hệ thống và công nghệ web - 15A", 70, [self._instructors[5],self._instructors[8],self._instructors[11],self._instructors[12],self._instructors[17],self._instructors[19],self._instructors[23],self._instructors[25],self._instructors[28]])
        course28 = Course("LHP28", "Hệ thống và công nghệ web - 15B", 70, [self._instructors[5],self._instructors[8],self._instructors[11],self._instructors[12],self._instructors[17],self._instructors[19],self._instructors[23],self._instructors[25],self._instructors[28]])
        course29 = Course("LHP29", "Hệ thống và công nghệ web - 15C", 70, [self._instructors[5],self._instructors[8],self._instructors[11],self._instructors[12],self._instructors[17],self._instructors[19],self._instructors[23],self._instructors[25],self._instructors[28]])
        course30 = Course("LHP30", "Xác định yêu cầu hệ thống - 15A", 60, [self._instructors[6],self._instructors[7],self._instructors[10],self._instructors[15],self._instructors[17],self._instructors[21],self._instructors[24],self._instructors[27],self._instructors[30]])
        course31 = Course("LHP31", "Xác định yêu cầu hệ thống - 15B", 60, [self._instructors[6],self._instructors[7],self._instructors[10],self._instructors[15],self._instructors[17],self._instructors[21],self._instructors[24],self._instructors[27],self._instructors[30]])
        course32 = Course("LHP32", "Xác định yêu cầu hệ thống - 15C", 60, [self._instructors[6],self._instructors[7],self._instructors[10],self._instructors[15],self._instructors[17],self._instructors[21],self._instructors[24],self._instructors[27],self._instructors[30]])
        course33 = Course("LHP33", "Mạng máy tính - 15A", 70, [self._instructors[6],self._instructors[9],self._instructors[10],self._instructors[11],self._instructors[13],self._instructors[19],self._instructors[24],self._instructors[25],self._instructors[29]])
        course34 = Course("LHP34", "Mạng máy tính - 15B", 70, [self._instructors[6],self._instructors[9],self._instructors[10],self._instructors[11],self._instructors[13],self._instructors[19],self._instructors[24],self._instructors[25],self._instructors[29]])
        course35 = Course("LHP35", "Cấu trúc rời rạc - 15A", 80, [self._instructors[6],self._instructors[7],self._instructors[15],self._instructors[16],self._instructors[19],self._instructors[21],self._instructors[22],self._instructors[27],self._instructors[28]])
        course36 = Course("LHP36", "Cấu trúc rời rạc - 15B", 80, [self._instructors[6],self._instructors[7],self._instructors[15],self._instructors[16],self._instructors[19],self._instructors[21],self._instructors[22],self._instructors[27],self._instructors[28]])
        course37 = Course("LHP37", "Cấu trúc rời rạc - 15C", 80, [self._instructors[6],self._instructors[7],self._instructors[15],self._instructors[16],self._instructors[19],self._instructors[21],self._instructors[22],self._instructors[27],self._instructors[28]])
        course38 = Course("LHP38", "Vật lí đại cương - 15A", 70, [self._instructors[7],self._instructors[8],self._instructors[9],self._instructors[12],self._instructors[14],self._instructors[17],self._instructors[20],self._instructors[23],self._instructors[26]])
        course39 = Course("LHP39", "Vật lí đại cương - 15B", 70, [self._instructors[7],self._instructors[8],self._instructors[9],self._instructors[12],self._instructors[14],self._instructors[17],self._instructors[20],self._instructors[23],self._instructors[26]])
        course40 = Course("LHP40", "Vật lí đại cương - 15C", 70, [self._instructors[7],self._instructors[8],self._instructors[9],self._instructors[12],self._instructors[14],self._instructors[17],self._instructors[20],self._instructors[23],self._instructors[26]])
        course41 = Course("LHP41", "Công nghệ phần mềm - 15A", 70, [self._instructors[8],self._instructors[9],self._instructors[10],self._instructors[11],self._instructors[13],self._instructors[14],self._instructors[15],self._instructors[16],self._instructors[18]])
        course42 = Course("LHP42", "Công nghệ phần mềm - 15B", 70, [self._instructors[8],self._instructors[9],self._instructors[10],self._instructors[11],self._instructors[13],self._instructors[14],self._instructors[15],self._instructors[16],self._instructors[18]])
        course43 = Course("LHP43", "Công nghệ phần mềm - 15C", 70, [self._instructors[8],self._instructors[9],self._instructors[10],self._instructors[11],self._instructors[13],self._instructors[14],self._instructors[15],self._instructors[16],self._instructors[18]])
        course44 = Course("LHP44", "Cơ sở dữ liệu - 15A", 70, [self._instructors[8],self._instructors[9],self._instructors[10],self._instructors[11],self._instructors[13],self._instructors[14],self._instructors[15],self._instructors[16],self._instructors[18]])
        course45 = Course("LHP45", "Cơ sở dữ liệu - 15B", 70, [self._instructors[8],self._instructors[9],self._instructors[10],self._instructors[11],self._instructors[13],self._instructors[14],self._instructors[15],self._instructors[16],self._instructors[18]])
        course46 = Course("LHP46", "Cơ sở dữ liệu - 15C", 70, [self._instructors[8],self._instructors[9],self._instructors[10],self._instructors[11],self._instructors[13],self._instructors[14],self._instructors[15],self._instructors[16],self._instructors[18]])
        course47 = Course("LHP47", "Hệ điều hành - 15A", 70, [self._instructors[8],self._instructors[9],self._instructors[10],self._instructors[11],self._instructors[13],self._instructors[14],self._instructors[15],self._instructors[17],self._instructors[27]])
        course48 = Course("LHP48", "Hệ điều hành - 15B", 70, [self._instructors[8],self._instructors[9],self._instructors[10],self._instructors[11],self._instructors[13],self._instructors[14],self._instructors[15],self._instructors[17],self._instructors[27]])
        course49 = Course("LHP49", "Logic học - 15A", 80, [self._instructors[9],self._instructors[12],self._instructors[13],self._instructors[15],self._instructors[17],self._instructors[18],self._instructors[23],self._instructors[25],self._instructors[30]])
        course50 = Course("LHP50", "Logic học - 15B", 80, [self._instructors[9],self._instructors[12],self._instructors[13],self._instructors[15],self._instructors[17],self._instructors[18],self._instructors[23],self._instructors[25],self._instructors[30]])
        course51 = Course("LHP51", "Logic học - 15C", 80, [self._instructors[9],self._instructors[12],self._instructors[13],self._instructors[15],self._instructors[17],self._instructors[18],self._instructors[23],self._instructors[25],self._instructors[30]])
        course52 = Course("LHP52", "Thực tập doanh nghiệp - 15A", 70, [self._instructors[9],self._instructors[11],self._instructors[12],self._instructors[13],self._instructors[15],self._instructors[24],self._instructors[25],self._instructors[27],self._instructors[29]])
        course53 = Course("LHP53", "Thực tập doanh nghiệp - 15B", 70, [self._instructors[9],self._instructors[11],self._instructors[12],self._instructors[13],self._instructors[15],self._instructors[24],self._instructors[25],self._instructors[27],self._instructors[29]])
        course54 = Course("LHP54", "Thực tập doanh nghiệp - 15C", 70, [self._instructors[9],self._instructors[11],self._instructors[12],self._instructors[13],self._instructors[15],self._instructors[24],self._instructors[25],self._instructors[27],self._instructors[29]])
        course55 = Course("LHP55", "Tiếng Việt thực hành - 15A", 60, [self._instructors[9],self._instructors[15],self._instructors[17],self._instructors[18],self._instructors[23],self._instructors[25],self._instructors[28],self._instructors[29],self._instructors[30]])
        course56 = Course("LHP56", "Tiếng Việt thực hành - 15B", 60, [self._instructors[9],self._instructors[15],self._instructors[17],self._instructors[18],self._instructors[23],self._instructors[25],self._instructors[28],self._instructors[29],self._instructors[30]])
        course57 = Course("LHP57", "Tiếng Việt thực hành - 15C", 60, [self._instructors[9],self._instructors[15],self._instructors[17],self._instructors[18],self._instructors[23],self._instructors[25],self._instructors[28],self._instructors[29],self._instructors[30]])
        course58 = Course("LHP58", "Quản trị học - 15A", 70, [self._instructors[7],self._instructors[9],self._instructors[11],self._instructors[12],self._instructors[13],self._instructors[15],self._instructors[22],self._instructors[27],self._instructors[28]])
        course59 = Course("LHP59", "Quản trị học - 15B", 70, [self._instructors[7],self._instructors[9],self._instructors[11],self._instructors[12],self._instructors[13],self._instructors[15],self._instructors[22],self._instructors[27],self._instructors[28]])
        course60 = Course("LHP60", "Quản trị học - 15C", 70, [self._instructors[7],self._instructors[9],self._instructors[11],self._instructors[12],self._instructors[13],self._instructors[15],self._instructors[22],self._instructors[27],self._instructors[28]])
        
        
        
        
        
        self._courses = [course1,course2,course3,course4,course5,course6,course7,course8,course9,course10,course11,course12,course13,course14,course15,course16,course17,course18,course19,course20,course21,course22,course23,course24,course25,course26,course27,course28,course29,course30,course31,course32,course33,course34,course35,course36,course37,course38,course39,course40,course41,course42,course43,course44,course45,course46,course47,course48,course49,course50,course51,course52,course53,course54,course55,course56,course57,course58,course59,course60]

        subject1 = Subject("MHP1", "Toán cao cấp",[course1,course2], 45)
        subject2 = Subject("MHP2", "Kỹ thuật lập trình",[course3,course4,course5], 60)
        subject3 = Subject("MHP3", "Triển khai hệ thống an ninh",[course6,course7,course8], 60)
        subject4 = Subject("MHP4", "Cấu trúc dữ liệu và giải thuật",[course9,course10,course11], 60)
        subject5 = Subject("MHP5", "Định tuyến và chuyển mạch",[course12,course13,course14], 60)
        subject6 = Subject("MHP6", "Công nghệ mới",[course15,course16], 60)
        subject7 = Subject("MHP7", "Lý thuyết đồ thị",[course17,course18,course19], 60)
        subject8 = Subject("MHP8", "Phân tích và thiết kế hệ thống",[course20,course21], 60)
        subject9 = Subject("MHP9", "Trí tuệ nhân tạo",[course22,course23], 60)
        subject10 = Subject("MHP10", "Hệ cơ sở dữ liệu",[course24,course25,course26], 60)
        subject11 =Subject("MHP11", "Hệ thống và công nghệ web",[course27,course28,course29], 60)
        subject12 = Subject("MHP12", "Xác định yêu cầu hệ thống",[course30,course31,course32], 60)
        subject13 = Subject("MHP13", "Mạng máy tính",[course33,course34], 60)
        subject14 = Subject("MHP14", "Cấu trúc rời rạc",[course35,course36,course37], 60)
        subject15 = Subject("MHP15", "Vật lí đại cương",[course38,course39,course40], 60)
        subject16 = Subject("MHP16", "Công nghệ phần mềm",[course41,course42,course43], 60)
        subject17 = Subject("MHP17", "Cơ sở dữ liệu",[course44,course45,course46], 60)
        subject18 = Subject("MHP18", "Hệ điều hành",[course47,course48], 60)
        subject19 = Subject("MHP19", "Logic học",[course49,course50,course51], 60)
        subject20 = Subject("MHP20", "Thực tập doanh nghiệp",[course52,course53,course54], 90)
        subject21 = Subject("MHP21", "Tiếng Việt thực hành",[course55,course56,course57], 60)
        subject22 = Subject("MHP22", "Quản trị học",[course58,course59,course60], 60)

        self._subjects = [subject1,subject2,subject3,subject4,subject5,subject6,subject7,subject8,subject9,subject10,subject11,subject12,subject13,subject14,subject15,subject16,subject17,subject18,subject19,subject20,subject21,subject22]
# -----------------------------------------------
        # for i in range(0, len(self.SUBJECT)):
        #     self._courses.append(Course(
        #         "L" + str(i+1), self.SUBJECT[i][0], 60, random_elements_list(self._instructors, 7)))

        # for i in range(0, len(self.SUBJECT),3):
        #     self._subjects.append(Subject(
        #         "MHP" + str(i), self.SUBJECT[i][1], [self._courses[i],self._courses[i+1],self._courses[i+2]], 3))
        
        for i in range(0, len(self._subjects)):
            self._numberCourseOfSubjects += len(self._subjects[i].get_courses())
#------------------------------------------------
    SUBJECT = [
        ['TKHTAN1', 'Triển khai hệ thống an ninh'], ['TKHTAN2', 'Triển khai hệ thống an ninh'], ['TKHTAN3', 'Triển khai hệ thống an ninh'], ['CTDLVGT1', 'Cấu trúc dữ liệu và giải thuật'], ['CTDLVGT2', 'Cấu trúc dữ liệu và giải thuật'], ['CTDLVGT3', 'Cấu trúc dữ liệu và giải thuật'], ['ĐTVCM1', 'Định tuyến và chuyển mạch'], ['ĐTVCM2', 'Định tuyến và chuyển mạch'], ['ĐTVCM3', 'Định tuyến và chuyển mạch'], ['CNM1', 'Công nghệ mới'], ['CNM2', 'Công nghệ mới'], ['CNM3', 'Công nghệ mới'], ['LTĐT1', 'Lý thuyết đồ thị'], ['LTĐT2', 'Lý thuyết đồ thị'], ['LTĐT3', 'Lý thuyết đồ thị'], ['PTVTKHT1', 'Phân tích và thiết kế hệ thống'], ['PTVTKHT2', 'Phân tích và thiết kế hệ thống'], ['PTVTKHT3', 'Phân tích và thiết kế hệ thống'], ['TTNT1', 'Trí tuệ nhân tạo'], ['TTNT2', 'Trí tuệ nhân tạo'], ['TTNT3', 'Trí tuệ nhân tạo'], ['HCSDL1', 'Hệ cơ sở dữ liệu'], ['HCSDL2', 'Hệ cơ sở dữ liệu'], ['HCSDL3', 'Hệ cơ sở dữ liệu'], ['HTVCNW1', 'Hệ thống và công nghệ web'], ['HTVCNW2', 'Hệ thống và công nghệ web'], ['HTVCNW3', 'Hệ thống và công nghệ web'], ['KTLT1', 'Kỹ thuật lập trình'], [
            'KTLT2', 'Kỹ thuật lập trình'], ['KTLT3', 'Kỹ thuật lập trình'], ['XĐYCHT1', 'Xác định yêu cầu hệ thống'], ['XĐYCHT2', 'Xác định yêu cầu hệ thống'], ['XĐYCHT3', 'Xác định yêu cầu hệ thống'], ['MMT1', 'Mạng máy tính'], ['MMT2', 'Mạng máy tính'], ['MMT3', 'Mạng máy tính'], ['CTRR1', 'Cấu trúc rời rạc'], ['CTRR2', 'Cấu trúc rời rạc'], ['CTRR3', 'Cấu trúc rời rạc'], ['KTMT1', 'Kiến trúc máy tính'], ['KTMT2', 'Kiến trúc máy tính'], ['KTMT3', 'Kiến trúc máy tính'], ['PPLNCKH1', 'Phương pháp luận nghiên cứu khoa học'], ['PPLNCKH2', 'Phương pháp luận nghiên cứu khoa học'], ['PPLNCKH3', 'Phương pháp luận nghiên cứu khoa học'], ['LTHĐT1', 'Lập trình hướng đối tượng'], ['LTHĐT2', 'Lập trình hướng đối tượng'], ['LTHĐT3', 'Lập trình hướng đối tượng'], ['TCC21', 'Toán cao cấp 2'], ['TCC22', 'Toán cao cấp 2'], ['TCC23', 'Toán cao cấp 2'], ['LH1', 'Logic học'], ['LH2', 'Logic học'], ['LH3', 'Logic học'], ['VLĐC1', 'Vật lí đại cương'], ['VLĐC2', 'Vật lí đại cương'], ['VLĐC3', 'Vật lí đại cương'], ['TTDN1', 'Thực tập doanh nghiệp'], ['TTDN2', 'Thực tập doanh nghiệp'], ['TTDN3', 'Thực tập doanh nghiệp']
    ]

    ROOMS = [
        ["P1", "A1.01", 60, "Lý thuyết"],
        ["P2", "A2.01", 70, "Lý thuyết"],
        ["P3", "A3.01", 65, "Thực hành"],
        ["P4", "A4.01", 65, "Lý thuyết"],
        ["P5", "A5.01", 60, "Thực hành"],
        ["P6", "A6.01", 60, "Thực hành"],
        ["P7", "A7.01", 70, "Lý thuyết"],
        ["P8", "A8.01", 65, "Thực hành"],
        ["P9", "A9.01", 60, "Thực hành"],
        ["P10", "A10.01", 60, "Lý thuyết"],
        ["P11", "A11.01", 65, "Thực hành"],
        ["P12", "A12.01", 75, "Thực hành"],
        ["P13", "A13.01", 70, "Lý thuyết"],
        ["P14", "A14.01", 65, "Thực hành"],
        ["P15", "A15.01", 65, "Lý thuyết"],
        ["P16", "A16.01", 60, "Thực hành"],
        ["P17", "A17.01", 65, "Lý thuyết"],
        ["P18", "A18.01", 70, "Thực hành"],
        ["P19", "A19.01", 60, "Lý thuyết"],
        ["P20", "A20.01", 65, "Thực hành"],
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
            "0953781926",  "1717 Nguyễn Văn Hữu"],
         ["GV16", "Trần Thị Ngọc", "Nữ", "tranthingoc@gmail.com", "0987654321", "101A Lê Lợi"],
        ["GV17", "Nguyễn Văn Hải", "Nam", "nguyenvanhai@gmail.com", "0976543210", "202B Đinh Tiên Hoàng"],
         ["GV18", "Phạm Thị Tuyết", "Nữ", "phamthituyet@gmail.com", "0965432109", "303C Trần Hưng Đạo"],
         ["GV19", "Lê Văn Đức", "Nam", "levanduc@gmail.com", "0954321098", "404D Nguyễn Văn Cừ"],
        ["GV20", "Trần Thị Hà", "Nữ", "tranthiha@gmail.com", "0943210987", "505E Lý Tự Trọng"],
        ["GV21", "Nguyễn Văn Minh", "Nam", "nguyenvanminh@gmail.com", "0932109876", "606F Phan Đình Phùng"],
         ["GV22", "Hoàng Thị Kim", "Nữ", "hoangthikim@gmail.com", "0921098765", "707G Nguyễn Trãi"],
        ["GV23", "Lê Văn Hùng", "Nam", "levanhung@gmail.com", "0910987654", "808H Nguyễn Hữu Thọ"],
         ["GV24", "Phạm Thị Lan", "Nữ", "phamthilan@gmail.com", "0909876543", "909I Lê Duẩn"],
        ["GV25", "Trần Văn Huy", "Nam", "tvanhuy@gmail.com", "0898765432", "1010J Hùng Vương"],
         ["GV26", "Nguyễn Thị Nhung", "Nữ", "nguyenthinhung@gmail.com", "0987654321", "1111K Phạm Văn Đồng"],
         ["GV27", "Lê Thị Kim", "Nữ", "lethikim@gmail.com", "0976543210", "1212L Trần Quốc Toản"],
         ["GV28", "Đinh Văn Bình", "Nam", "dinhvanbinh@gmail.com", "0965432109", "1313M Nguyễn Văn Trỗi"],
         ["GV29", "Nguyễn Văn Tùng", "Nam", "nguyenvantung@gmail.com", "0954321098", "1414N Trần Đại Nghĩa"],
         ["GV30", "Phạm Thị Hương", "Nữ", "phamthihuong@gmail.com", "0943210987", "1515O Trần Hưng Đạo"],
         ["GV31", "Phạm Thị Tố Nữ", "Nữ", "phamthitonu@gmail.com", "094325457", "1O Trần Hưng Đạo"]
    ]

    TIMELESSONS = [
            ["T213", "Thứ Hai 06:30 - 09:00"],
            ["T246", "Thứ Hai 09:00 - 11:30"],
            ["T279", "Thứ Hai 12:30 - 15:00"],
            ["T21012", "Thứ Hai 15:00 - 17:30"],
            ["T313", "Thứ Ba 06:30 - 09:00"],
            ["T346", "Thứ Ba 09:00 - 11:30"],
            ["T379", "Thứ Ba 12:30 - 15:00"],
            ["T31012", "Thứ Ba 15:00 - 17:30"],
            ["T413", "Thứ Tư 06:30 - 09:00"],
            ["T446", "Thứ Tư 09:00 - 11:30"],
            ["T479", "Thứ Tư 12:30 - 15:00"],
            ["T41012", "Thứ Tư 15:00 - 17:30"],
            ["T513", "Thứ Năm 06:30 - 09:00"],
            ["T546", "Thứ Năm 09:00 - 11:30"],
            ["T579", "Thứ Năm 12:30 - 15:00"],
            ["T51012", "Thứ Năm 15:00 - 17:30"],
            ["T613", "Thứ Sáu 06:30 - 09:00"],
            ["T646", "Thứ Sáu 09:00 - 11:30"],
            ["T679", "Thứ Sáu 12:30 - 15:00"],
            ["T61012", "Thứ Sáu 15:00 - 17:30"]
            ]
    
    
    def get_rooms(self):
        return self._rooms
        
    def get_instructors(self):
        return self._instructors

    def get_time_lessons(self):
        return self._timeLessons

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
        self.print_instructors()
        self.print_courses()
        self.print_rooms()
        self.print_time_lessons()

    def print_subjects(self):
        x = PrettyTable()
        subjects = self._data.get_subjects()
        print("--- Bảng thông tin môn học ---")
        x.field_names = ["STT", "Mã môn học", "Tên môn học", "Lớp học phần", "Số tiết"]
        for i in range (0,len(subjects)):
            courses = subjects[i].get_courses()
            tempStr = '['
            for j in range (0,len(courses)-1):
                tempStr += courses[j].get_name() + ','
            tempStr += courses[len(courses)-1].get_name() + ']'
            x.add_row([str(i+1), subjects[i].get_id(), subjects[i].get_name(), tempStr, str(subjects[i].get_numberOfCredits())])
        print(x)
    
    def print_instructors(self):
        x = PrettyTable()
        instructors = self._data.get_instructors()
        print("--- Bảng thông tin giảng viên ---")
        x.field_names = ["STT", "Mã giảng viên", "Tên giảng viên", "Giới tính", "Email", "Số điện thoại", "Địa chỉ"]
        for i in range (0,len(instructors)):
            x.add_row([str(i+1),instructors[i].get_id(),instructors[i].get_name(),instructors[i].get_sex(),instructors[i].get_email(),instructors[i].get_phone(),instructors[i].get_address()])
        print(x)

    def print_courses(self):
        x = PrettyTable()
        courses = self._data.get_courses()
        print("--- Bảng thông tin lớp học phần ---")
        x.field_names = ["STT", "Mã lớp học phần", "Tên lớp học phần", "Số lượng sinh viên", "Giảng viên"]
        for i in range (0,len(courses)):
            instructors = courses[i].get_instructors()
            tempStr = '['
            for j in range (0,len(instructors)-1):
                tempStr += instructors[j].get_name() + ','
            tempStr += instructors[len(instructors)-1].get_name() + ']'
            x.add_row([str(i+1),courses[i].get_id(),courses[i].get_name(),str(courses[i].get_maxNumberOfStudents()),tempStr])
        print(x)

    def print_rooms(self):
        x = PrettyTable()
        rooms = self._data.get_rooms()
        print("--- Bảng thông tin phòng học ---")
        x.field_names = ["STT", "Mã phòng học", "Tên phòng học", "Số lượng chỗ ngồi", "Loại phòng học"]
        for i in range (0,len(rooms)):
            x.add_row([str(i+1),rooms[i].get_id(),rooms[i].get_name(),str(rooms[i].get_capacity()),rooms[i].get_type()])
        print(x)    

    def print_time_lessons(self):
        x = PrettyTable()
        timeLessons = self._data.get_time_lessons()
        print("--- Bảng thông tin thời gian học ---")
        x.field_names = ["STT", "Mã thời gian học", "Thời gian học"]
        for i in range (0,len(timeLessons)):
            x.add_row([str(i+1),timeLessons[i].get_id(),timeLessons[i].get_time()])
        print(x)

    def print_schedule(self,schedule):
        x = PrettyTable()
        print("--- Bảng thời khóa biểu ---")
        x.field_names = ["STT", "Môn học(id)", "Lớp học phần(maxNumberOfStudents)", "Room(capacity)", "Giảng viên(id)", "Thời gian(id)"]
        classes = schedule.get_classes()
        for i in range (0,len(classes)):
            x.add_row([str(i+1),
                       classes[i].get_subject().get_name() + '(' + classes[i].get_subject().get_id()+')', 
                       classes[i].get_course().get_id() + '(' + str(classes[i].get_course().get_maxNumberOfStudents())+')',
                       classes[i].get_room().get_name() + '('+ str(classes[i].get_room().get_capacity())+')', 
                       classes[i].get_instructors().get_name()  + '(' + classes[i].get_instructors().get_id()+')', 
                       classes[i].get_time().get_time() + '(' + classes[i].get_time().get_id()+')'])
        print(x)
    
    def print_generation(self,population):
        x = PrettyTable()
        print("--- Bảng thế hệ (fitness) ---")
        x.field_names = ["STT","Fitness","Conflicts","Thời khóa biểu([Classes])"]
        for i in range (0, len(population)):
            classes = population[i].get_classes()
            x.add_row([str(i),population[i].get_fitness(),population[i].get_numberOfConflicts(),[str(x) for x in classes]])
            # [str(x) for x in  classes]
        x.align["Thời khóa biểu([Classes])"] = "l"
        x.max_width["Thời khóa biểu([Classes])"] = 120
        print(x)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Population:
    def __init__(self, population_size):
        self._population_size = population_size
        self._schedules = []
        schedule = [Schedule(data).create_schedule() for i in range(population_size)]
        self._schedules = schedule
    def get_schedules(self):
        return self._schedules

class GA:
    def selection(self, population):
        # Chọn ngẫu nhiên 2 cá thể trong quần thể
        schedule1 = random.choice(population)
        schedule2 = random.choice(population)
        # Chọn cá thể có fitness cao hơn
        if schedule1.get_fitness() > schedule2.get_fitness():
            return schedule1
        return schedule2
    
    def crossover(self, parent1, parent2):
        schedule_crossover = Schedule(data).createSchedule()
        # Sinh ngẫu nhiên điểm cắt
        cut_point = random.randint(0, len(parent1.get_classes()) - 1)
        length1 = len(parent1.get_classes())
        length2 = len(parent2.get_classes())
        for i in range(0,len(parent1.get_classes())):
            # Sinh con 1 từ phần đầu của parent1 và phần sau của parent2
            classes1 = parent1.get_classes()[random.randint(0,length1)][:cut_point] + parent2.get_classes()[random.randint(0,length2)][cut_point:]
            schedule_crossover[i].append(classes1)
        return schedule_crossover
    
    def crossover_population(self, population):
        population_crossover = Population(0).get_schedules()
        for i in range (0,len(population)):
            schedule1 = self.selection(population)
            schedule2 = self.selection(population)
            population_crossover.append(self.crossover(schedule1,schedule2))
        return population_crossover

    def mutation(self, schedule_mutation,mutation_rate):
        schedule = Schedule(data).createSchedule()
        for i in range (schedule_mutation.get_classes()):
            if(mutation_rate < random.randint(0,100)):
                schedule_mutation.get_classes()[i] = schedule.get_classes()[i]
        return schedule_mutation

    def mutation_population (self, population,mutation_rate):
        for i in range (0,len(population)):
            self.mutation(population[i],mutation_rate)
        return population
    
    def run(self, population,mutation_rate):
        return self.mutation_population(self.crossover_population(population),mutation_rate)
        
data = Data()
def main():
    display = Display(data)
    # xác định dân số ban đầu của quần thể
    population_size = 20
    # xác định số thế hệ (lần lặp lại) thuật toán
    num_generations = 0
    print('Số thế hệ: ', num_generations)
    best_fitness = 0

    # Tạo quần thể ban đầu
    schedules = Population(population_size).get_schedules()
    # display.print_schedule(schedules[0])
    # # Khởi tạo và chạy thuật toán GA
    # ga = GA()
    # start_time = time.time()
    # while(num_generations<= 100):
    #     num_generations += 1
    #     print('Số thế hệ: ', num_generations)
    #     best_schedule = ga.run(schedules,10)
    # end_time = time.time()
    # print("Thời gian chạy thuật toán: ", end_time - start_time, " giây")
    # display.print_schedule(best_schedule)
    # print(schedules[0].get_classes()[random.randint(0,len(schedules[0].get_classes()))][:2] + schedules[1].get_classes()[random.randint(0,len(schedules[0].get_classes()))][2:])
    display.print_schedule(schedules[0])
    display.print_generation(schedules)
if __name__ == "__main__":
    main()

