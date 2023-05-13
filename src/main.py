import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time

from ga.gas import GA
from ga.population import Population


def main():
    best_fitness = 0
    # xác định dân số ban đầu của quần thể
    population_size = 20
    # xác định số thế hệ (lần lặp lại) thuật toán
    num_generations = 20000
    # Tỉ lệ đột biến
    mutation_rate = 0.05
    # Tỉ lệ lai ghép
    crossover_rate = 0.8
    elitism_rate = 0.05


    # Tạo quần thể ban đầu
    population = Population(population_size).get_schedules()
    ga = GA(population, mutation_rate, crossover_rate, elitism_rate)
    # Bắt đầu đếm thời gian
    start = time.time()
    ga.run(num_generations)
    # Kết thúc đếm thời gian
    end = time.time()
    print('Thời gian chạy: ', end - start)
    
if __name__ == "__main__":
    main()