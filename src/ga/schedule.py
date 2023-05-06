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
        self.calc_fitness()
        
    def get_courses(self):
        return self.courses
    
    def get_rooms(self):
        return self.rooms
    
    def get_timelessons(self):
        return self.timelessons

    def get_classes(self):
        return self.classes

    def get_fitness(self):
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
        for i in range(len(self.classes)):
            if self.classes[i].get_room().get_room_capacity() < self.classes[i].get_course().get_max_students():
                self.conflict += 1
            for j in range(i+1, len(self.classes)):
                if self.classes[i].get_timelesson() == self.classes[j].get_timelesson() and self.classes[i].get_id() != self.classes[j].get_id():
                    if self.classes[i].get_room() == self.classes[j].get_room():
                        self.conflict += 1
                    # if self.classes[i].get_course() == self.classes[j].get_course():
                    #     self.conflict += 1
        self.fitness = 1 / (self.conflict + 1)