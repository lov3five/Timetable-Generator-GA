
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.courses import *
from db.connect import *
from db.rooms import *
from db.service import *
from db.timelessons import *

def courses_per_resource(courses, rooms, time_lessons):
    return ("courses_per_resource: {} / {}".format(len(courses), len(rooms) * len(time_lessons)))

info_ga = courses_per_resource(courses_db, rooms_db, timelessons_db)