import os
import sys
# Thêm đường dẫn vào `sys.path`
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from ga.population import Population

class GA:
    def __init__(self, population, mutation_rate, crossover_rate, elitism_rate):
        self.population = population
        self.mutation_rate = mutation_rate # tỷ lệ đột biến
        self.crossover_rate = crossover_rate # tỷ lệ lai chéo
        self.elitism_rate = elitism_rate # tỷ lệ elitism
        
    def evolve(self):
        # Sort population by fitness
        self.population.sort(key=lambda x: x.get_fitness(), reverse=True)

        print('Số lượng schedule trong quần thể: ', len(self.population))
        print('Best schedule fitness: ', self.population[0].get_fitness())
        print('Conflicts: ', self.population[0].get_conflict())
        # Create new population
        new_population = Population(0).get_schedules()
        
        # Thêm các cá thể ưu tú vào quần thể mới
        num_elite = int(self.elitism_rate * len(self.population))
        new_population.extend(self.population[:num_elite])
        
        # Crossover
        while len(new_population) < len(self.population):
            parent1, parent2 = self.select_parents()
            
            if random.random() < self.crossover_rate:
                schedule_crossover = self.crossover(parent1, parent2)
            else:
                schedule_crossover = parent1
            new_population.append(schedule_crossover)
        
        # Mutation
        for individual in new_population:
            if random.random() < self.mutation_rate:
                self.mutate(individual)
        
        # Update population
        self.population = new_population
    
    def select_parents(self):
        # Tournament selection
        tournament_size = 5
        tournament = random.sample(self.population, tournament_size)
        tournament.sort(key=lambda x: x.get_fitness(), reverse=True)
        parent1 = tournament[0]
        parent2 = tournament[1]
        return parent1, parent2
    
    def crossover(self, parent1, parent2):
        # #Uniform Crossover
        # schedule_crossover = Population(1).get_schedules()[0]
        # for i in range (0,len(schedule_crossover.get_classes())):
        #     if(random.random() > 0.5):
        #         schedule_crossover.get_classes()[i] = parent1.get_classes()[i]
        #     else:
        #         schedule_crossover.get_classes()[i] = parent2.get_classes()[i]
        # return schedule_crossover

        # Single Point Crossover
        schedule_crossover = Population(1).get_schedules()[0]
        crossover_point = random.randint(0, len(schedule_crossover.get_classes())-1)
        for i in range (0,len(schedule_crossover.get_classes())):
            if i < crossover_point:
                schedule_crossover.get_classes()[i] = parent1.get_classes()[i]
            else:
                schedule_crossover.get_classes()[i] = parent2.get_classes()[i]
        return schedule_crossover
    
        # #Multi-point Crossover
        # schedule_crossover = Population(1).get_schedules()[0]
        # num_points = 5
        # points = sorted(random.sample(range(len(schedule_crossover.get_classes())), num_points))
        # index = 0
        # for i in range (0,len(schedule_crossover.get_classes())):
        #     if i in points:
        #         index += 1
        #     if index % 2 == 0:
        #         schedule_crossover.get_classes()[i] = parent1.get_classes()[i]
        #     else:
        #         schedule_crossover.get_classes()[i] = parent2.get_classes()[i]
        # return schedule_crossover

    
    def mutate(self, individual):
        schedule_mutate = Population(1).get_schedules()[0]
        print(schedule_mutate.get_classes())
        for i in range (0,len(schedule_mutate.get_classes())):
            if(random.random() > self.mutation_rate):
                schedule_mutate.get_classes()[i] = individual.get_classes()[i]
        return schedule_mutate
    
    def run(self,num_generations):
        for i in range (0,num_generations):
            print('Số thế hệ: ', i)
            self.evolve()
        return self.population
