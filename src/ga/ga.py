import random
import numpy as np

class GA: 
    def __init__(self, classes, courses, timelesson, population_size, mutation_probability):
        self.classes = classes
        self.courses = courses
        self.timelesson = timelesson
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.population = []
        self.fitness_scores = []
        self.best_timetable = None
        self.best_fitness = None