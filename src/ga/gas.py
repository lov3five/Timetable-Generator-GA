import os
import sys
# Thêm đường dẫn vào `sys.path`
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random

class GA:
    def __init__(self, population, mutation_rate, crossover_rate, elitism_rate):
        self.population = population
        self.mutation_rate = mutation_rate # tỷ lệ đột biến
        self.crossover_rate = crossover_rate # tỷ lệ lai chéo
        self.elitism_rate = elitism_rate # tỷ lệ elitism
        
    def evolve(self):
        # Sort population by fitness
        self.population.sort(key=lambda x: x.fitness, reverse=True)
        
        # Create new population
        new_population = []
        
        # Elitism - keep the top individuals
        num_elite = int(self.elitism_rate * len(self.population))
        new_population.extend(self.population[:num_elite])
        
        # Crossover
        while len(new_population) < len(self.population):
            parent1, parent2 = self.select_parents()
            
            if random.random() < self.crossover_rate:
                child1, child2 = self.crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
                
            new_population.append(child1)
            if len(new_population) < len(self.population):
                new_population.append(child2)
        
        # Mutation
        for individual in new_population:
            if random.random() < self.mutation_rate:
                self.mutate(individual)
        
        # Update population
        self.population = new_population
    
    def select_parents(self):
        # Tournament selection
        tournament_size = 2
        tournament = random.sample(self.population, tournament_size)
        tournament.sort(key=lambda x: x.fitness, reverse=True)
        parent1 = tournament[0]
        parent2 = tournament[1]
        return parent1, parent2
    
    def crossover(self, parent1, parent2):
        # Single point crossover
        crossover_point = random.randint(1, len(parent1.schedule)-2)
        child1 = Classes(parent1.schedule[:crossover_point] + parent2.schedule[crossover_point:])
        child2 = Classes(parent2.schedule[:crossover_point] + parent1.schedule[crossover_point:])
        return child1, child2
    
    def mutate(self, individual):
        # Random mutation
        mutation_point1 = random.randint(0, len(individual.schedule)-1)
        mutation_point2 = random.randint(0, len(individual.schedule)-1)
        individual.schedule[mutation_point1], individual.schedule[mutation_point2] = individual.schedule[mutation_point2], individual.schedule[mutation_point1]
