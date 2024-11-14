import random as rd
from operator import itemgetter

def create_random_chromosomes(size, n) -> list: 
    list_of_chromosomes = []
    for i in range(n):
        list_of_chromosomes.append(rd.sample(range(size), size))
    for i in range(n):
        list_of_chromosomes[i].append(0)
    return list_of_chromosomes


def cross_over(list_of_chromosomes, size) -> list:
    rd.shuffle(list_of_chromosomes)
    n = len(list_of_chromosomes)
    for i in range(0, n, 2):
        first_child = list_of_chromosomes[i][: size//2] 
        for j in range(size):
            if list_of_chromosomes[i + 1][j] not in first_child:
                first_child.append(list_of_chromosomes[i + 1][j])
        if len(first_child) != size:
            print('fuck meeeee', first_child, '      ', list_of_chromosomes[i], list_of_chromosomes[i + 1], i)
            return
        second_child = list_of_chromosomes[i + 1][: size//2] 
        for j in range(size):
            if list_of_chromosomes[i][j] not in second_child:
                second_child.append(list_of_chromosomes[i][j])
        first_child.append(0)
        second_child.append(0)
        list_of_chromosomes.append(first_child)
        list_of_chromosomes.append(second_child)
        if len(list_of_chromosomes[0]) != size + 1:
            print('its my faulttt', list_of_chromosomes[0])
            return
    return list_of_chromosomes


def calculate_fitness(list_of_chromosomes) -> list:
    n = len(list_of_chromosomes)
    for chromosome in list_of_chromosomes:
        fitness = chromosome_fitness(chromosome)
        chromosome[-1] = fitness
    return list_of_chromosomes


def chromosome_fitness(chromosome) -> int:
    score = 0
    for i in range(len(chromosome)):
        for j in range(i+1, len(chromosome)):
            if chromosome[i] == chromosome[j]:
                score += 1
            elif abs(i - j) == abs(chromosome[i] - chromosome[j]):
                score += 1
    return (size * (size - 1)) / 2 - score


def eliminate(list_of_chromosomes):
    n = len(list_of_chromosomes)
    list_of_chromosomes = sorted(list_of_chromosomes, key = itemgetter(-1))
    list_of_chromosomes = list_of_chromosomes[n // 2:]
    maximum = list_of_chromosomes[-1][-1]
    return (list_of_chromosomes, maximum)
    

def mutation(list_of_chromosomes, mutation_rate, size) -> list:
    n = len(list_of_chromosomes)
    for i in range(n//2, n):
        if rd.random() <= mutation_rate:
            indexes = rd.sample(range(size), 2)
            a = list_of_chromosomes[i][indexes[0]] 
            b = list_of_chromosomes[i][indexes[1]]
            list_of_chromosomes[i][indexes[0]] = b
            list_of_chromosomes[i][indexes[1]] = a
    return list_of_chromosomes


size = 10
max_fitness = (size * (size - 1)) / 2 
maximum = 0
mutation_rate = 0.5
population = create_random_chromosomes(size, 50)
generation = 1

while maximum < max_fitness:
    population = cross_over(population, size)
    population = calculate_fitness(population)
    population = mutation(population, mutation_rate, size)
    population, maximum = eliminate(population)
    print('generation: ', generation, '    maximun fitness: ', maximum)
    generation += 1

print(population[-1][: -1])

