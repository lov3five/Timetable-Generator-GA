# Hàm khởi tạo quần thể ban đầu
def initialize_population(population_size, data):
    population = []
    for i in range(population_size):
        schedule = Schedule(data).create_schedule()
        population.append(schedule)
    return population

# Hàm đánh giá độ thích nghi của giải pháp
def fitness(schedule):
    # Tính toán độ phù hợp của giải pháp theo tiêu chí nào đó
    # Ví dụ: tính tổng số lượng xung đột giữa các lớp học trong lịch
    return fitness_score

# Hàm chọn lọc giải pháp cha mẹ
def selection(population, num_parents):
    parents = []
    # Thực hiện phương pháp chọn lọc phù hợp để lựa chọn giải pháp cha mẹ
    return parents

# Hàm lai ghép
def crossover(parents, offspring_size):
    offspring = []
    for i in range(offspring_size):
        # Thực hiện phương pháp lai ghép để tạo ra giải pháp con mới
        offspring.append(offspring_schedule)
    return offspring

# Hàm đột biến
def mutation(schedule_mutation, mutation_rate):
    schedule = Schedule(data).create_schedule()
    for i in range(len(schedule_mutation.get_classes())):
        if mutation_rate < random.randint(0, 100):
            schedule_mutation.get_classes()[i] = schedule.get_classes()[i]
    return schedule_mutation

# Hàm kiểm tra điều kiện dừng
def is_termination_condition_met(current_generation, max_generations):
    return current_generation > max_generations

# Hàm thực hiện thuật toán di truyền
def genetic_algorithm(data, population_size, max_generations, mutation_rate, num_parents):
    # Khởi tạo quần thể ban đầu
    population = initialize_population(population_size, data)

    # Vòng lặp cho đến khi điều kiện dừng được đáp ứng
    current_generation = 1
    while not is_termination_condition_met(current_generation, max_generations):
        # Tính độ thích nghi của từng giải pháp trong quần thể
        fitness_scores = [fitness(schedule) for schedule in population]

        # Chọn lọc giải pháp cha mẹ
        parents = selection(population, num_parents)

        # Lai ghép giải pháp cha mẹ để tạo ra giải pháp con mới
        offspring = crossover(parents, len(population) - len(parents))

        # Thực hiện đột biến trên giải pháp con mới
        mutated_offspring = [mutation(schedule, mutation_rate) for schedule in offspring]

        # Tính độ thích nghi của từng giải pháp mới
        mutated_offspring_fitness_scores = [fitness(schedule) for schedule in mutated_offspring]

        # Tổng hợp lại quần thể mới bao gồm giải pháp cha mẹ và giải pháp con mới
        population = parents + mutated_offspring

        # LINE 1
    old_population_conflicts = sum(fitness_scores)

    # Tính toán tổng số lượng xung đột giữa các lớp học trong quần thể mới
    new_population_conflicts = sum(mutated_offspring_fitness_scores)

    # Tìm giải pháp tốt nhất trong quần thể mới
    best_solution_index = mutated_offspring_fitness_scores.index(min(mutated_offspring_fitness_scores))
    best_solution = mutated_offspring[best_solution_index]

    # Tìm giải pháp tốt nhất trong quần thể cũ
    individual_best_fitness = min(fitness_scores)
    individual_best_solution_index = fitness_scores.index(individual_best_fitness)
    individual_best_solution = population[individual_best_solution_index]
    
    # Nếu giải pháp tốt nhất trong quần thể mới tốt hơn giải pháp tốt nhất trong quần thể cũ
    if individual_best_fitness > mutated_offspring_fitness_scores[best_solution_index]:
        population = mutated_offspring
    else:
        # Lựa chọn giải pháp tốt nhất trong quần thể cũ và thêm vào quần thể mới
        population = population[:individual_best_solution_index] + population[individual_best_solution_index+1:]
        population.append(individual_best_solution)
    
    # In ra kết quả tại thế hệ hiện tại
    print("Generation:", current_generation, "\tBest Solution:", individual_best_fitness)

    # Tăng thế hệ hiện tại lên 1
    current_generation += 1

# Trả về giải pháp tốt nhất tìm được
return individual_best_solution

# LINE 2
# Vòng lặp cho đến khi điều kiện dừng được đáp ứng
current_generation = 1
while not is_termination_condition_met(current_generation, max_generations):
    # Tính độ thích nghi của từng giải pháp trong quần thể
    fitness_scores = [fitness(schedule) for schedule in population]

    # Chọn lọc giải pháp cha mẹ
    parents = selection(population, num_parents)

    # Lai ghép giải pháp cha mẹ để tạo ra giải pháp con mới
    offspring = crossover(parents, len(population) - len(parents))

    # Thực hiện đột biến trên giải pháp con mới
    mutated_offspring = [mutation(schedule, mutation_rate) for schedule in offspring]

    # Tính độ thích nghi của từng giải pháp mới
    mutated_offspring_fitness_scores = [fitness(schedule) for schedule in mutated_offspring]

    # Tổng hợp lại quần thể mới bao gồm cả cha mẹ và con cái
    population = parents + mutated_offspring

    # Tăng biến đếm thế hệ hiện tại lên 1
    current_generation += 1

# Trả về giải pháp tốt nhất
best_schedule_index = fitness_scores.index(max(fitness_scores))
best_schedule = population[best_schedule_index]
return best_schedule

def tournament_selection(self, population):
        if(len(population) % 2 == 0):
            tournament_size = int(len(population)*(1/5))
        else:
            tournament_size = int(len(population)*(1/3))
        tournament_population = Population(0)
        i = 0
        while i < tournament_size:
            tournament_population.get_schedules().append(population.get_schedules()[random.randint(0,len(population.get_schedules())-1)])
            i += 1
        tournament_population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_population