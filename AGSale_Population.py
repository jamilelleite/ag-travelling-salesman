import numpy as np
import AGSale_DNA
import random

class Population:
    def __init__(self, number_cities, mutRate, sizePop, number_generations, cities):
        self.cities = cities
        self.world_record = 0
        self.best = 0
        self.size_population = sizePop
        self.population = []
        self.number_generations = number_generations
        self.matingPool = []
        self.mutRate = mutRate
        self.number_cities = number_cities
        for i in range(0, self.size_population):
            self.population.append(AGSale_DNA.DNA(number_cities))
        
    def calc_fitness(self):
        for i in range(self.size_population):
            self.population[i].fitness_function(self.cities)

    def natural_selection(self):
        max_fitness = 0
        self.matingPool = []

        for i in range(self.size_population):
            if self.population[i].fitness_score > max_fitness:
                max_fitness = self.population[i].fitness_score

        #fitne ja deve ter sido calculado
        for i in range(self.size_population):
            n_pool = int((self.population[i].fitness_score * 1000)/max_fitness)
            for n in range(n_pool):
                self.matingPool.append(self.population[i])

    def generate(self):
        size_mating_pool = len(self.matingPool)
        for i in range(self.size_population):
            a = random.randrange(0, size_mating_pool)
            b = random.randrange(0, size_mating_pool)
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutRate)
            self.population[i] = child

    def get_best(self):
       for i in range(self.size_population):
            if self.population[i].fitness_score > self.world_record:
                # index_world_record = i
                self.world_record = self.population[i].fitness_score
                self.best = self.population[i]
            


        
