from matplotlib import pyplot as plt
from numpy.random import choice
import numpy as np
import random


class Problem2:
    def __init__(self):
        self.professions = {'Professional': [.63, .25, .12], 'Service': [.30, .45, .25], 'Manu': [.41, .41, .18]}
        l = list(self.professions.keys())
        self.individuals = [random.choice(l) for _ in range(100)]

    def long_term(self):
        gens = []
        for _ in range(50):
            gens.append(self.individuals.copy())
            self.compute_next_gen()
        self.counting(gens)
        return gens

    def compute_next_gen(self):
        test = []
        a = list(self.professions.keys())
        for individual in self.individuals:
            test.append(choice(a, 1, p=self.professions.get(individual))[0])
        self.individuals = test

    def counting(self, gens):
        service = 0
        professional = 0
        manu = 0
        total = 0
        for i, gen in enumerate(gens):
            service += len([profes for profes in gen if profes == 'Service'])
            professional += len([profes for profes in gen if profes == 'Professional'])
            manu += len([profes for profes in gen if profes == 'Manu'])
            total += len([profes for profes in gen if profes == 'Service'])
            total += len([profes for profes in gen if profes == 'Professional'])
            total += len([profes for profes in gen if profes == 'Manu'])
        print('Service', service / total, 'Professional', professional / total, 'Manufacturing', manu / total)

    @staticmethod
    def plot(gens):
        plt.figure()

        for i, gen in enumerate(gens):
            service = [profes for profes in gen if profes == 'Service']
            professional = [profes for profes in gen if profes == 'Professional']
            manu = [profes for profes in gen if profes == 'Manu']
            plt.bar(i - 0.2, len(professional), width=0.2, color='b', align='center')
            plt.bar(i, len(service), width=0.2, color='g', align='center')
            plt.bar(i + 0.2, len(manu), width=0.2, color='r', align='center')
        plt.show()


if __name__ == '__main__':
    problem2 = Problem2()
    print(problem2.long_term())
