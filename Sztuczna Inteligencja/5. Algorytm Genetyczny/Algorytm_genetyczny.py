import random

population_size = 6
mutation_rate = 0.1
max_generations = 100

population = [[0 for j in range(4)] for i in range(population_size)]
pairXY = [[-5, 150], [4, -77], [-3, -30], [-2, 0], [-1, 10], [0.5, 16.375], [1, 18], [2, 25], [3, 32], [4, 75], [5, 130]]

# Tworzenie populacji początkowej
for i in range(population_size):
    for j in range(4):
        population[i][j] = random.randint(-15, 15)


def activation_function(i):
    a, b, c, d = i
    e = sum(abs(a * pow(x, 3) + b * pow(x, 2) + c * x + d) for x, y in pairXY)
    return e


# Krzyżowanie rodziców
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


# Mutacja
def mutate(chromosome):
    mutated_chromosome = chromosome
    i = random.randint(0, 19)
    if random.random() <= mutation_rate:
        if mutated_chromosome[i] == '0':
            mutated_chromosome = mutated_chromosome[:i] + '1' + mutated_chromosome[i + 1:]
        else:
            mutated_chromosome = mutated_chromosome[:i] + '0' + mutated_chromosome[i + 1:]
    return mutated_chromosome


# Selekcja typu ruletka
def roulette_selection(population, activation_function):
    total = sum(activation_function)
    probabilities = [score / total for score in activation_function]
    selected = random.choices(population, probabilities, k=2)
    return selected[0], selected[1]


# Konwersja na binarny (chromosom)
def convert_to_binary(number):
    binary = ""
    for i in range(len(number)):
        if number[i] >= 0:
            first_bit = '1'
        else:
            first_bit = '0'

        binary = binary + first_bit + format(abs(number[i]), '04b')

    return binary


# Konwersja na liczbę
def convert_to_number(binary):
    numbers = []
    for i in range(0, len(binary), 5):
        first_bit = int(binary[i])
        bits = binary[i + 1:i + 5]
        if first_bit == 1:
            nr = int(bits, 2)
        else:
            nr = -int(bits, 2)
        numbers.append(nr)
    return numbers


# Algorytm genetyczny
def genetic_algorithm():
    global population

    for generation in range(max_generations):
        activation = [activation_function(i) for i in population]
        new_population = []

        for _ in range(population_size // 2):
            parent1, parent2 = roulette_selection(population, activation)
            child1, child2 = crossover(convert_to_binary(parent1), convert_to_binary(parent2))
            child1 = mutate(child1)
            child2 = mutate(child2)
            child1 = convert_to_number(child1)
            child2 = convert_to_number(child2)
            new_population.append(child1)
            new_population.append(child2)

        population = new_population

    best_individual = max(population, key=activation_function)
    return best_individual

print(f"Liczba generacji: {max_generations}")
print("\nPoczątkowe współczynniki: ")
print(f"{population[0]} \n{population[1]} \n{population[2]} \n{population[3]} \n{population[4]} \n{population[5]}")
print("\nPoczątkowe wyniki funkcji: ")
print(f"{activation_function(population[0])} \n{activation_function(population[1])} \n{activation_function(population[2])} "
      f"\n{activation_function(population[3])} \n{activation_function(population[4])} \n{activation_function(population[5])}")

result = genetic_algorithm()

print("\nKońcowe współczynniki: ")
print(f"{population[0]} \n{population[1]} \n{population[2]} \n{population[3]} \n{population[4]} \n{population[5]}")
print("\nKońcowe wyniki funkcji: ")
print(f"{activation_function(population[0])} \n{activation_function(population[1])} \n{activation_function(population[2])} "
      f"\n{activation_function(population[3])} \n{activation_function(population[4])} \n{activation_function(population[5])}")
print("\nNajlepsze końcowe współczynniki: ")
print(result)
print("\nNajlepszy końcowy wynik: ")
print(activation_function(result))
