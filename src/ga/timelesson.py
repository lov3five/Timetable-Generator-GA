import os
import sys
# Thêm đường dẫn vào `sys.path`
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TimeLesson:
    def __init__(self,id ,uuid, period):
        self.id = id
        self.uuid = uuid
        self.period = period
        
    def get_timelesson_id(self):
        return self.id
    
    def get_timelesson_uuid(self):
        return self.uuid
    
    def get_timelesson_period(self):
        return self.period
    
    def __str__(self):
        return f' {self.uuid} - {self.id} - {self.period}'
    
def init_timelessons(timelessons_db):
    timelessons = []
    for timelesson in timelessons_db:
        timelessons.append(TimeLesson(timelesson[0], timelesson[1], timelesson[2]))
    return timelessons

