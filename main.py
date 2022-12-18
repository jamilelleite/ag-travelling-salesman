import random
import numpy as np 
import math
import AGSale_DNA
import AGSale_Population

number_cities = 10
mutation_rate = 0.15
size_population = 100
number_generation = 200



def setup(number_cities, mutation_rate, size_population, number_generation, cities):
    popul = AGSale_Population.Population(number_cities, mutation_rate, size_population, number_generation, cities)
    popul.calc_fitness()
    print("\npopulacao aleatoria inicial:")
    for i in range(0, popul.size_population):
        print(popul.population[i].genes)
        print(popul.population[i].fitness_score)
    return popul

def draw(popul, number_generation):
    
    for i in range(0, number_generation):
        # print("\nGeracao: ", i)

        # print("\npopulacao aleatoria inicial:")
        # for i in range(0, popul.size_population):
        #     print(popul.population[i].genes)
        #     print(popul.population[i].fitness_score)


        popul.natural_selection()
        # print("\nMating Pool:")
        # for i in range(len(popul.matingPool)):
        #     print(popul.matingPool[i].genes)



        popul.generate()
        popul.calc_fitness()
        # print("\nNova populacao")
        # for i in range(popul.size_population):
        #     print(popul.population[i].genes)
        #     print(popul.population[i].fitness_score)

        popul.get_best()


cities = AGSale_DNA.Cities(number_cities)
print(cities)

popul = setup(number_cities, mutation_rate, size_population, number_generation, cities)

# print("\npopulacao aleatoria inicial:")
# for i in range(0, popul.size_population):
#     print(popul.population[i].genes)
#     print(popul.population[i].fitness_score)

# popul.natural_selection()
# print("\nMating Pool:")
# for i in range(len(popul.matingPool)):
#     print(popul.matingPool[i].genes)

# popul.generate()
# popul.calc_fitness()
# print("\nNova populacao")
# for i in range(popul.size_population):
#     print(popul.population[i].genes)
#     print(popul.population[i].fitness_score)

draw(popul, number_generation)
print("\nNova populacao")
for i in range(popul.size_population):
    print(popul.population[i].genes)
    print(popul.population[i].fitness_score)

print("best:")
print(popul.best.genes)
print(popul.best.fitness_score)






