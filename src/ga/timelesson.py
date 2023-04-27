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
        return "TimeLesson: " + self.id + " | " + self.uuid + " | " + self.period