import os
import sys
import random
# Thêm đường dẫn vào `sys.path`
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes import Classes

from db import timelessons_db
from db import rooms_db
from db import courses_db

from course import init_courses
from room import init_rooms
from timelesson import init_timelessons

courses = init_courses(courses_db)
rooms = init_rooms(rooms_db)
timelessons = init_timelessons(timelessons_db)

class Schedule:
    def __init__(self, courses, rooms, timelessons):
        self.courses = courses
        self.rooms = rooms
        self.timelessons = timelessons
        self.classes_id = 0
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
    
    def init_schedule(self):
        for i in range(len(self.courses)):
            self.classes.append(Classes(self.classes_id, self.courses[i], random.choice(self.rooms), random.choice(self.timelessons)))
            self.classes_id += 1
        self.calc_fitness()

    def calc_fitness(self):
        self.conflict = 0
        for i in range(len(self.classes)):
            print(self.classes[i].get_course().get_max_students())
            if self.classes[i].get_room().get_room_capacity() < self.classes[i].get_course().get_max_students():
                self.conflict += 1
            for j in range(i+1, len(self.classes)):
                if self.classes[i].get_timelesson() == self.classes[j].get_timelesson() and self.classes[i].get_id() != self.classes[j].get_id():
                    if self.classes[i].get_room() == self.classes[j].get_room():
                        self.conflict += 1
                    if self.classes[i].get_course() == self.classes[j].get_course():
                        self.conflict += 1
        self.fitness = 1 / (self.conflict + 1)
    
    def __str__(self):
        return f'Schedule: {self.classes} - Fitness: {self.fitness}'

schedule = Schedule(courses, rooms, timelessons).init_schedule()
print(schedule)

