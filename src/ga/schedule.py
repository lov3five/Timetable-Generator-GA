import os
import sys
import random
# Thêm đường dẫn vào `sys.path`
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
        self.genes = []
        self.fitness = 0

    def init_schedule(self):
        for course in self.courses:
            self.genes.append([course, random.choice(self.rooms), random.choice(self.timelessons)])
        return self.genes
    
    def caculate_fitness()


    