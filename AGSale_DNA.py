import numpy as np 
import random
import math 



def Cities(N):
    return np.random.randint(100, size=(N, 2)) #cidade por x.y
    #instancia cities

# cities = Cities(5)
# print("\nLocalizacao cidades:")
# print(cities)

class DNA:
    def __init__(self, N):
        self.genes = np.arange(N)
        np.random.shuffle(self.genes)
        self.fitness_score = 0
        

    def fitness_function(self, cities):
        score = 0
        for i in range(self.genes.size - 1):
            score += math.sqrt(math.pow(cities[self.genes[i]][0] - cities[self.genes[i+1]][0], 2) + math.pow(cities[self.genes[i]][1] - cities[self.genes[i+1]][1],2))
        self.fitness_score =  1000 - score

    def crossover(self, partner):  #DNA partner
        child = DNA(self.genes.size)

        # valid = 0
        # cont = 0

        midpoint = random.randrange(self.genes.size)


        # while not valid:
        for i in range(self.genes.size):
            if i < midpoint:
                child.genes[i] = self.genes[i]
            else:
                # child.genes[i] = partner.genes[i]
                for j in range(partner.genes.size):
                    if partner.genes[j]  not in child.genes[:i]:
                        child.genes[i] = partner.genes[j]
                        break
            
            # aux_genes = np.unique(child.genes)    # tentativa correcao repeticao
            # cont = cont + 1
            # if aux_genes.size == self.N:
            #     valid = 1
        # print("contador: ", cont)

        return child

    def mutate(self, mutationRate):
        aux = random.randrange(100)
        if  aux < mutationRate*100:
            a = random.randrange(self.genes.size)
            b = random.randrange(self.genes.size)
            self.genes[[a,b]] = self.genes[[b,a]]

# dna1 = DNA(5)
# print("\nIndividuo 1:")
# print("\nOrdem cidades 1")
# print(dna1.genes)
# dna1.fitness_function()
# print("\nFitness score 1:")
# print(dna1.fitness_score)

# dna2 = DNA(5)
# print("\nIndividuo 2:")
# print("\nOrdem cidades 2")
# print(dna2.genes)
# dna2.fitness_function()
# print("\nFitness score 2:")
# print(dna2.fitness_score)

# child = dna1.crossover(dna2)
# print("\nIndividuo Filho:")
# print("\nOrdem cidades Filho")
# print(child.genes)
# child.fitness_function()
# print("\nFitness score Filho:")
# print(child.fitness_score)

# child.mutate(0.5)
# print("\nFilho pos mut")
# print(child.genes)





