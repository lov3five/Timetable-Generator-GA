import random
import time

from prettytable import PrettyTable


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
        return "Classes: " + str(self._stt) + " | " + str(self._subject.get_name()) + " | " + str(self._course.get_name()) + " | " + str(self._room.get_name()) 

class Schedule:
    def __init__(self,data):
        self._data = data
        self._classes = []
        self._fitness = 0
        self._numberOfConflicts = 0
        self._idCLasses = 0
        
    def createSchedule(self):
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
    def calculate_fitness(self):
        self._numberOfConflicts = 0
        classes = self.get_classes()
        for i in range(0,len(classes)):
            # Kiểm tra xem phòng có đủ chỗ không
            if(classes[i].get_room().get_capacity() < classes[i].get_course().get_maxNumberOfStudents()):
                self._numberOfConflicts += 1
        return self._numberOfConflicts

    def get_fitness(self):
        return self._fitness

    def get_numberOfConflicts(self):
        return self._numberOfConflicts
    
    def get_classes(self):
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
            self._rooms.append(ClassRoom(
                self.ROOMS[i][0], self.ROOMS[i][1], self.ROOMS[i][2], self.ROOMS[i][3]))

        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(
                self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1], self.INSTRUCTORS[i][2], self.INSTRUCTORS[i][3], self.INSTRUCTORS[i][4], self.INSTRUCTORS[i][5]))

        for i in range(0, len(self.TIMELESSONS)):
            self._timeLessons.append(TimeLessons(
                self.TIMELESSONS[i][0], self.TIMELESSONS[i][1]))
        course1 = Course("LHP1", "Toán cao cấp - 15A", 60,[self._instructors[0],self._instructors[1]])
        course2 = Course("LHP2", "Toán cao cấp - 15B", 70, [self._instructors[0],self._instructors[1],self._instructors[2]])
        course3 = Course("LHP3", "Kỹ thuật lập trình - 15A",60, [self._instructors[1],self._instructors[2]])
        course4 = Course("LHP4", "Kỹ thuật lập trình - 15B", 70, [self._instructors[0],self._instructors[2]])
        self._courses = [course1,course2,course3,course4]
        subject1 = Subject("MHP1", "Toán cao cấp",[course1,course2], 45)
        subject2 = Subject("MHP2", "Kỹ thuật lập trình",[course3,course4], 60)
        self._subjects = [subject1,subject2]
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
        ["P2", "A2.01", 61, "Lý thuyết"],
        ["P3", "A3.01", 62, "Thực hành"],
        ["P4", "A4.01", 63, "Thực hành"],
    ]

    INSTRUCTORS = [
        ["GV1", "Nguyễn Thị Thảo", "Nữ", "nguyenthithao@gmail.com",
            "0956446246",  "303 Phạm Văn Đồng"],
        ["GV2", "Trần Văn Tài", "Nam", "tvantai@gmail.com",
            "0963847221",  "404 Trần Đại Nghĩa"],
        ["GV3", "Nguyễn Văn An", "Nam", "nguyenvanan@gmail.com",
            "0976488312",  "505 Nguyễn Văn Cừ"],
        ["GV4", "Phạm Thị Hoa", "Nữ", "phamthihoa@gmail.com",
            "0968597831",  "606 Trần Hưng Đạo"]
    ]

    TIMELESSONS = [["TG1", "Thứ Hai 06:30 - 09:00"],
                   ["TG2", "Thứ Hai 09:00 - 11:30"],
                   ["TG3", "Thứ Hai 12:30 - 15:00"],
                   ["TG4", "Thứ Hai 15:00 - 17:30"]]
    
    
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
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Population:
    def __init__(self, population_size, data):
        self._population_size = population_size
        self._data = data
        self._schedules = []
        
        schedule = [Schedule(data).createSchedule() for i in range(population_size)]
        self._schedules = schedule
    def get_schedules(self):
        return self._schedules

class GA:
    def selection(self, population):
        # Chọn ngẫu nhiên 2 cá thể trong quần thể
        individual1 = random.choice(population)
        individual2 = random.choice(population)
        # Chọn cá thể có fitness cao hơn
        if individual1.get_fitness() > individual2.get_fitness():
            return individual1
        return individual2

    def crossover(self, parent1, parent2):
        # Sinh ngẫu nhiên điểm cắt
        cut_point = random.randint(0, len(parent1.get_classes()) - 1)
        # Sinh con 1 từ phần đầu của parent1 và phần sau của parent2
        child1 = parent1.get_classes()[:cut_point] + parent2.get_classes()[cut_point:]
        # Sinh con 2 từ phần đầu của parent2 và phần sau của parent1
        child2 = parent2.get_classes()[:cut_point] + parent1.get_classes()[cut_point:]
        return child1, child2

    def mutation(self, individual):
        # Sinh ngẫu nhiên điểm cắt
        cut_point = random.randint(0, len(individual.get_classes()) - 1)
        # Sinh ngẫu nhiên một giá trị mới cho gene tại điểm cắt
        individual.get_classes()[cut_point] = random.randint(0, 1)
        return individual

    def run(self, population):
        # Chọn 2 cá thể
        parent1 = self.selection(population)
        parent2 = self.selection(population)
        # Sinh con
        child1, child2 = self.crossover(parent1, parent2)
        # Sinh ngẫu nhiên một số nguyên trong khoảng [0, 100]
        mutation_rate = random.randint(0, 100)
        # Nếu số nguyên sinh ra nhỏ hơn 10 thì thực hiện mutation
        # Tỷ lệ xảy ra đột biến là 10%
        if mutation_rate < 10:
            child1 = self.mutation(child1)
            child2 = self.mutation(child2)
        

def main():
    data = Data()
    display = Display(data)
    display.print_all_data()
    # xác định dân số ban đầu của quần thể
    population_size = 2
    # xác định số thế hệ (lần lặp lại) thuật toán
    num_generations = 0

    best_schedule = None
    best_fitness = 0

    # Tạo quần thể ban đầu
    population = Population(population_size, data).get_schedules()
    # Khởi tạo và chạy thuật toán GA
    # ga = GA()
    # start_time = time.time()
    # ga.run(population)
    # end_time = time.time()
    # print("Thời gian chạy thuật toán: ", end_time - start_time, " giây")
    display.print_schedule(population[0])
if __name__ == "__main__":
    main()

