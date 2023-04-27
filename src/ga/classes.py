class Classes:
    def __init__(self, id, course_id, room_id, timelesson_id):
        self.id = id
        self.course_id = course_id
        self.room_id = room_id
        self.timelesson_id = timelesson_id
        
    def get_classes_id(self):
        return self.id
    
    def set_classes_id(self, id):
        self.id = id
    
    def get_course_id(self):
        return self.course_id
    
    def set_course_id(self, course_id):
        self.course_id = course_id
    
    def get_room_id(self):
        return self.room_id
    
    def set_room_id(self, room_id):
        self.room_id = room_id
    
    def get_timelesson_id(self):
        return self.timelesson_id
    
    def set_timelesson_id(self, timelesson_id):
        self.timelesson_id = timelesson_id
    
    def __str__(self):
        return "Class: " + str(self.id) + " Course: " + str(self.course_id) + " Room: " + str(self.room_id) + " Time: " + str(self.timelesson_id)