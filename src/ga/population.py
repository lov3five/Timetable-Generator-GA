import os
import sys

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

from schedule import Schedule
from utils import pretty_table_for_class

class Population:
    def __init__(self, population_size):
        self.population_size = population_size
        self.schedules = [Schedule().init_schedule(courses, rooms, timelessons) for _ in range(population_size)]
        self.fittest = None
        
    def get_schedules(self):
        return self.schedules
    
    def get_fittest(self):
        return self.fittest

    def set_fittest(self, fittest):
        self.fittest = fittest
        
    def get_population_size(self):
        return self.population_size
    
    def __str__(self):
        return f"Population size: {self.population_size} -  - Fittest: {self.fittest}"
    
# populations = Population(2)
# print(populations.get_population_size())
# schedules = populations.get_schedules()


