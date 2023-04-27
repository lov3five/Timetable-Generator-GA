class Schedule:
    def __init__(self, courses, rooms, timelessons):
        self.courses = courses
        self.rooms = rooms
        self.timelessons = timelessons
        self.genes = []
        for course in courses:
            gene = (course, random.choice(rooms), random.choice(timelessons))
            self.genes.append(gene)


schedule = Schedule(courses, rooms, timelessons)
