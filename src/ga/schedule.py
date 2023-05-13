import os
import sys
# Thêm đường dẫn vào `sys.path`
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from ga.classes import Classes

class Schedule:
    # Counter_id: đếm số lượng Classes (PK)
    counter_classes_id = 0
    
    def __init__(self, courses, rooms, timelessons):
        self.courses = courses
        self.rooms = rooms
        self.timelessons = timelessons
        self.classes = []
        self.fitness = 0
        self.conflict = 0
        self.is_fitness_changed = False
        
        
    def get_courses(self):
        return self.courses
    
    def get_rooms(self):
        return self.rooms
    
    def get_timelessons(self):
        return self.timelessons

    def get_classes(self):
        self.is_fitness_changed = True
        return self.classes

    def get_fitness(self):
        if(self.is_fitness_changed):
            self.fitness = self.calc_fitness()
            self.is_fitness_changed = False
        return self.fitness
        
    def get_conflict(self):
        return self.conflict
    
    # Hiển thị dữ liệu của Schedule: tôi muốn hiển thị danh sách Classes, fitness
    def __str__(self):
        output = ""
        for i in range(len(self.classes) - 1):
            output += str(self.classes[i]) + "\n"
        output += str(self.classes[-1])
        return output + " - Fitness: " + str(self.fitness)
    
    def init_schedule(self):
        for i in range(len(self.courses)):
            self.classes.append(Classes(self.counter_classes_id, self.courses[i], random.choice(self.rooms), random.choice(self.timelessons)))
            # Counter_id: tăng lên 1
            Schedule.counter_classes_id += 1
        self.calc_fitness()
        return self
        

    def calc_fitness(self):
        self.conflict = 0
        classes = self.get_classes()
        for i in range(len(self.classes)):
            # print("A: ",self.classes[i].get_room().get_room_capacity())
            # print("B: ",self.classes[i].get_course().get_max_students())
            if classes[i].get_room().get_room_capacity() < classes[i].get_course().get_max_students():
                self.conflict += 1
            for j in range(i+1, len(self.classes)):
                # Kiểm tra tại 1 phòng có 2 lớp học cùng 1 thời điểm không
                if classes[i].get_timelesson() == classes[j].get_timelesson() and classes[i].get_id() != classes[j].get_id():
                    if classes[i].get_room() == classes[j].get_room():
                        self.conflict += 1
                # Kiểm tra 1 giảng viên có dạy 2 lớp cùng 1 lúc
                if classes[i].get_timelesson() == classes[j].get_timelesson() and classes[i].get_id() != classes[j].get_id():
                    if classes[i].get_course().get_instructor_id() == classes[j].get_course().get_instructor_id():
                        self.conflict += 1
        return 1 / (self.conflict + 1)