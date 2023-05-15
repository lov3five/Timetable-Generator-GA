import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time

from ga.population import Population
from ga.gas import GA

from utils import sound_notification

from prettytable import PrettyTable

def main():
    best_fitness = 0
    # xác định dân số ban đầu của quần thể
    population_size = 30
    
    # xác định số thế hệ (lần lặp lại) thuật toán
    num_generations = 20000
    # Tỉ lệ đột biến
    mutation_rate = 0.05 # 0.01 - 0.1
    # Tỉ lệ lai ghép
    crossover_rate = 0.85  # 0.6 - 0.9
    elitism_rate = 0.01 # 0.05 - 0.1

    # Tạo quần thể ban đầu
    start_time = time.time()
    population = Population(population_size).get_schedules()
    ga = GA(population, mutation_rate, crossover_rate, elitism_rate)
    
    ga.run(num_generations)
        # Lấy ra kết quả tốt nhất
    best_schedule = ga.get_population()
    for schedule in best_schedule:
        list_conflict_of_schedule = []
        list_fitness_of_schedule = []
        list_conflict_of_schedule.append(schedule.get_conflict())
        list_fitness_of_schedule.append(schedule.get_fitness())
    list_schedule_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        
    x = PrettyTable()
    x.field_names = ["Schedule ID", "Conflict", "Fitness"]
    for i in range(len(list_schedule_id)):
        x.add_row([list_schedule_id[i], list_conflict_of_schedule[i], list_fitness_of_schedule[i]])
    print(x)

        
    
    
    print("Best schedule: ", best_schedule[0])
     
    end_time = time.time()
    print("Time: ", end_time - start_time)
    while ga.get_population()[0].get_conflict() == 0 :
        sound_notification()
    


if __name__ == "__main__":
    main()