import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time

from ga.population import Population
from ga.gas import GA

from utils import sound_notification

def main():
    best_fitness = 0
    # xác định dân số ban đầu của quần thể
    population_size = 20
    # xác định số thế hệ (lần lặp lại) thuật toán
    num_generations = 20000
    # Tỉ lệ đột biến
    mutation_rate = 0.05 # 0.01 - 0.1
    # Tỉ lệ lai ghép
    crossover_rate = 0.8  # 0.6 - 0.9
    elitism_rate = 0.05 # 0.05 - 0.1

    # Tạo quần thể ban đầu
    start_time = time.time()
    population = Population(population_size).get_schedules()
    ga = GA(population, mutation_rate, crossover_rate, elitism_rate)
    
    ga.run(num_generations)
    end_time = time.time()
    print("Time: ", end_time - start_time)
    while ga.get_population()[0].get_conflict() == 0 :
        sound_notification()
    
    # # Lấy ra kết quả tốt nhất
    # best_schedule = ga.get_population()
    
    # # In ra kết quả tốt nhất
    # print(best_schedule)

if __name__ == "__main__":
    main()