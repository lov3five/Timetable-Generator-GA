import os
import sys
# Thêm đường dẫn vào `sys.path`
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from ga.population import Population
from db import info_ga

# class GA:
#     def __init__(self, population, mutation_rate, crossover_rate, elitism_rate):
#         self.population = population
#         self.mutation_rate = mutation_rate # tỷ lệ đột biến
#         self.crossover_rate = crossover_rate # tỷ lệ lai chéo
#         self.elitism_rate = elitism_rate # tỷ lệ tinh túy
        
#     def evolve(self):
#         # Sort population by fitness
#         self.population.sort(key=lambda x: x.get_fitness(), reverse=True)

#         print('Số lượng schedule trong quần thể: ', len(self.population))
#         print('Best schedule fitness: ', round(self.population[0].get_fitness(), 3))
#         print('Conflicts:', [schedule.get_conflict() for schedule in self.population[:10]])
#         # Create new population
#         new_population = Population(0).get_schedules()
        
#         # Thêm các cá thể ưu tú vào quần thể mới
#         num_elite = int(self.elitism_rate * len(self.population))
#         new_population.extend(self.population[:num_elite])
        
#         # Crossover
#         while len(new_population) < len(self.population):
#             parent1, parent2 = self.select_parents()
            
#             if random.random() < self.crossover_rate:
#                 schedule_crossover = self.crossover(parent1, parent2)
#             else:
#                 schedule_crossover = parent1
#             new_population.append(schedule_crossover)
        
#         # Mutation
#         for individual in new_population:
#             if random.random() < self.mutation_rate:
#                 self.mutate(individual)
        
#         # # Mutation
#         # for i in range(num_elite, len(new_population)):
#         #     if random.random() < self.mutation_rate:
#         #         self.mutate(new_population[i])
            
        
#         # Update population
#         self.population = new_population
    
#     def select_parents(self):
#         # Tournament selection
#         tournament_size = 4
#         tournament = random.sample(self.population, tournament_size)
#         tournament.sort(key=lambda x: x.get_fitness(), reverse=True)
#         parent1 = tournament[0]
#         parent2 = tournament[1]
#         return parent1, parent2
    
#     def crossover(self, parent1, parent2):
#         # # Uniform Crossover
#         # schedule_crossover = Population(1).get_schedules()[0]
#         # for i in range (0,len(schedule_crossover.get_classes())):
#         #     if(random.random() > 0.5):
#         #         schedule_crossover.get_classes()[i] = parent1.get_classes()[i]
#         #     else:
#         #         schedule_crossover.get_classes()[i] = parent2.get_classes()[i]
#         # return schedule_crossover

#         # # Single Point Crossover
#         # schedule_crossover = Population(1).get_schedules()[0]
#         # crossover_point = random.randint(0, len(schedule_crossover.get_classes())-1)
#         # for i in range (0,len(schedule_crossover.get_classes())):
#         #     if i < crossover_point:
#         #         schedule_crossover.get_classes()[i] = parent1.get_classes()[i]
#         #     else:
#         #         schedule_crossover.get_classes()[i] = parent2.get_classes()[i]
#         # return schedule_crossover
    
#         #Multi-point Crossover
#         schedule_crossover = Population(1).get_schedules()[0]
#         num_points = 9
#         points = sorted(random.sample(range(len(schedule_crossover.get_classes())), num_points))
#         index = 0
#         for i in range (0,len(schedule_crossover.get_classes())):
#             if i in points:
#                 index += 1
#             if index % 2 == 0:
#                 schedule_crossover.get_classes()[i] = parent1.get_classes()[i]
#             else:
#                 schedule_crossover.get_classes()[i] = parent2.get_classes()[i]
#         return schedule_crossover

    
#     def mutate(self, individual):
#         schedule_mutate = Population(1).get_schedules()[0]
#         for i in range (0,len(schedule_mutate.get_classes())):
#             if(random.random() > self.mutation_rate):
#                 individual.get_classes()[i] = schedule_mutate.get_classes()[i]
#         return individual

    
#     def run(self,num_generations):
#         for i in range (0,num_generations):
#             print('Số thế hệ: ', i)
#             print(info_ga)
#             self.evolve()
#         return self.population
import pandas as pd
# Hàm can thiệp 
def add_dataframe_to_excel(file_path, new_sheet_name, df):
    """
    Thêm một DataFrame vào một trang tính mới của một tệp Excel đã có các trang tính.

    Parameters:
    file_path (str): Đường dẫn đến tệp Excel.
    new_sheet_name (str): Tên của trang tính mới.
    df (pandas.DataFrame): DataFrame cần thêm vào trang tính mới.

    Returns:
    pandas.DataFrame: DataFrame mới được tạo từ tệp Excel đã cập nhật.
    """
    # Ghi DataFrame mới vào trang tính mới của tệp Excel đã có sẵn
    with pd.ExcelWriter(file_path,engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name=new_sheet_name, index=False)

    # Đọc tệp Excel đã cập nhật và trả về DataFrame mới
    with pd.ExcelFile(file_path) as xls:
        sheet_names = xls.sheet_names
        dfs = []
        for sheet_name in sheet_names:
            df = pd.read_excel(xls, sheet_name)
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

class GA:
    def __init__(self, population, mutation_rate, crossover_rate, elitism_rate):
        self.population = population
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_rate = elitism_rate
        self.prev_conflict = None
        self.unchanged_count = 0
        self.list_conflict = []
        self.list_generation = []
    
        
    def get_population(self):
        return self.population
        
    def evolve(self):
        # Biến đếm số thế hệ liên tiếp mà giá trị conflict không thay đổi
        
        
        # Sort population by fitness
        self.population.sort(key=lambda x: x.get_fitness(), reverse=True)
        
        self.list_conflict.append(self.population[0].get_conflict())

        print('Số lượng schedule trong quần thể: ', len(self.population))
        print('Best schedule fitness: ', round(self.population[0].get_fitness(), 3))
        print('Conflicts:', [schedule.get_conflict() for schedule in self.population[:20]])
        
        current_conflict = self.population[0].get_conflict()
        print("==================================================")
        print('Số conflict trước của best schedule: ', self.prev_conflict)
        print('Số conflict hiện tại của best schedule: ', current_conflict)
        # Kiểm tra nếu số conflict không thay đổi qua 50 thế hệ
        if current_conflict == self.prev_conflict:
            self.unchanged_count += 1  
            print('Số thế hệ không thay đổi conflict: ', self.unchanged_count) 
        else:
            self.unchanged_count = 0
            
        
        # Lưu số thế hệ khi conflict không thay đổi
        self.prev_conflict = current_conflict
        
        # Create new population
        new_population = Population(0).get_schedules()
        
        # Thêm các cá thể ưu tú vào quần thể mới
        num_elite = int(self.elitism_rate * len(self.population))
        new_population.extend(self.population[:num_elite])

        #################
        """ CROSSOVER """
        while len(new_population) < len(self.population):
            parent1, parent2 = self.select_parents()
            crossover_random = [self.crossover_uniform(parent1, parent2), self.crossover_single_point(parent1, parent2), self.crossover_multi_point(parent1, parent2)]
            if random.random() < self.crossover_rate:
                schedule_crossover = crossover_random[0]
            else:
                schedule_crossover = parent1
            new_population.append(schedule_crossover)
            
        ################
        """ MUTATION """
        for individual in new_population:
            if random.random() < self.mutation_rate:
                self.mutate(individual)
        # Update population
        self.population = new_population
        
    
    def select_parents(self):
        # Tournament selection
        tournament_size = 6
        tournament = random.choices(self.population, k=tournament_size)
        tournament.sort(key=lambda x: x.get_fitness(), reverse=True)
        parent1 = tournament[0]
        parent2 = tournament[1]
        return parent1, parent2
    
    def crossover_uniform(self, parent1, parent2):
        # Uniform Crossover
        schedule_crossover = Population(1).get_schedules()[0]
        for i in range (0,len(schedule_crossover.get_classes())):
            if(random.random() > 0.5):
                schedule_crossover.get_classes()[i] = parent1.get_classes()[i]
            else:
                schedule_crossover.get_classes()[i] = parent2.get_classes()[i]
        return schedule_crossover
        
    
    def crossover_single_point(self, parent1, parent2):
        # Single Point Crossover
        schedule_crossover = Population(1).get_schedules()[0]
        crossover_point = random.randint(0, len(schedule_crossover.get_classes())-1)
        for i in range (0,len(schedule_crossover.get_classes())):
            if i < crossover_point:
                schedule_crossover.get_classes()[i] = parent1.get_classes()[i]
            else:
                schedule_crossover.get_classes()[i] = parent2.get_classes()[i]
        return schedule_crossover
    
    def crossover_multi_point(self, parent1, parent2):
        #Multi-point Crossover
        schedule_crossover = Population(1).get_schedules()[0]
        num_points = 40
        points = sorted(random.sample(range(len(schedule_crossover.get_classes())), num_points))
        index = 0
        for i in range (0,len(schedule_crossover.get_classes())):
            if i in points:
                index += 1
            if index % 2 == 0:
                schedule_crossover.get_classes()[i] = parent1.get_classes()[i]
            else:
                schedule_crossover.get_classes()[i] = parent2.get_classes()[i]
        return schedule_crossover


    # Hàm đột biến
    def mutate(self, individual):
        schedule_mutate = Population(1).get_schedules()[0]
        for i in range(len(schedule_mutate.get_classes())):
            if random.random() < self.mutation_rate:
                individual.get_classes()[i] = schedule_mutate.get_classes()[i]
        return individual

    def hill_climbing_mutation(self, individual):
        best_individual = individual
        best_fitness = individual.get_fitness()
    
        # Khởi tạo các thay đổi
        mutations = [(i, j) for i in range(len(individual.get_classes())) for j in range(len(individual.get_classes()))]
    
        while mutations:
            mutated_individual = individual
            i, j = mutations.pop(random.randrange(len(mutations)))
            mutated_individual.get_classes()[i], mutated_individual.get_classes()[j] = mutated_individual.get_classes()[j], mutated_individual.get_classes()[i]
        
            mutated_fitness = mutated_individual.get_fitness()
        
            if mutated_fitness > best_fitness:
                best_individual = mutated_individual
                best_fitness = mutated_fitness
        return best_individual
    
    def run(self, num_generations):
        for i in range(num_generations):
            print('Số thế hệ:', i)
            print(info_ga)
            self.list_generation.append(i)
            self.evolve()
            if self.population[0].get_conflict() == 0:
                list_conflict = self.list_conflict
                list_gene = self.list_generation
                add_dataframe_to_excel('output.xlsx', 'Conflict1', pd.DataFrame(list_conflict, columns=['conflict']))
                add_dataframe_to_excel('output.xlsx', 'Generation1', pd.DataFrame(list_gene, columns=['Generation']))
                break
            
                
        return self.population
    
    
