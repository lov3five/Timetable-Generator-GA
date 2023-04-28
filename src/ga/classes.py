
class Classes:
    def __init__(self, id, course, room, timelesson):
        self.id = id
        self.course = course 
        self.room = room
        self.timelesson = timelesson

        
    def get_id(self):
        return self.id
    
    def get_course(self):
        return self.course

    def get_room(self):
        return self.room
    
    def get_timelesson(self):
        return self.timelesson
    
    def __str__(self):
        return f'Class: {self.id} - Course: {self.course} - Room: {self.room} - Time: {self.timelesson}'
