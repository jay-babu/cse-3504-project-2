# Part D

import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable


class ProblemD:
    def __init__(self):
        self.scenario = np.array([[.1, .75, 0, 0, .15], [0, .1, .8, 0, .1], [
            0, 0, .15, .75, .1], [0, 0, 0, .1, .9], [0, 0, 0, 0, 1]])

    def simulate1(self):
        scenarios = []
        for i in range(1, 16, 1):
            i /= 100
            temp_scenario = np.copy(self.scenario)
            original = temp_scenario[0][-1]
            temp_scenario[0][-1] = i
            residual = original - i
            temp_scenario[0][0] += residual
            scenarios.append(temp_scenario)
            # print(temp_scenario)
        return scenarios

    def simulate2(self):
        scenarios = []
        for i in range(1, 16, 1):
            i /= 100
            temp_scenario = np.copy(self.scenario)
            original = temp_scenario[0][-1]
            temp_scenario[0][-1] = i
            residual = original - i
            temp_scenario[0][1] += residual
            scenarios.append(temp_scenario)
            # print(temp_scenario)
        return scenarios

    def simulate3(self):
        scenarios = []
        for i in range(1, 16, 1):
            i /= 100
            temp_scenario = np.copy(self.scenario)
            original = temp_scenario[0][-1]
            temp_scenario[0][-1] = i
            residual = original - i
            temp_scenario[0][0] += residual / 2
            temp_scenario[0][1] += residual / 2
            scenarios.append(temp_scenario)
            # print(temp_scenario)
        return scenarios

    def grad_prob(self, scenarios):
        freshman_graduations = []
        for scenario in scenarios:
            # freshman_s = scenario[0]
            # sophomore_s = scenario[1]
            # junior_s = scenario[2]
            senior_s = scenario[3]

            probability = 1
            for year in range(len(scenario) - 2):
                repeat = scenario[year][year]
                moving = scenario[year][year + 1]
                leave = scenario[year][-1]
                probability *= moving / (1 - repeat)

            repeat = senior_s[3]
            moving = .8
            leave = .1
            probability *= moving / (1 - repeat)
            freshman_graduations.append(probability)
            # print(probability)
        return freshman_graduations

    def scenario_to_q(self, scenarios):
        """
        Removing leave
        """
        new_scenarios = []
        for scenario in scenarios:
            new_scenario = []
            for i in range(len(scenario[:-1])):
                new_scenario.append(scenario[:-1][i][:-1])
            new_scenarios.append(new_scenario)
        return new_scenarios

    def i_minus_q(self, scenarios):
        inverses = []
        for scenario in scenarios:
            inverses.append(sum(np.linalg.inv(np.identity(4) - scenario)[0]))
        # print(inverses)
        return inverses

    def pp(self, scenarios):
        for scenario in scenarios:
            labels = ['', 'Freshman', 'Sophomore', 'Junior', 'Senior', 'Leave']
            table = PrettyTable(labels[:len(scenario) + 1])
            for i in range(len(scenario)):
                temp = list(scenario[i])
                temp.insert(0, labels[i + 1])
                table.add_row(temp)
            print(table)

    def pp_i(self, scenario):
        table = PrettyTable(['Probabilities %', 'Expectation'])
        # for i in range(len(scenario)):
        # temp = list(scenario)
        # temp.insert(0, labels)
        for i, expect in enumerate(scenario):
            table.add_row([i, expect])
        print(table)


if __name__ == "__main__":
    simulation = ProblemD()
    scenarios1 = simulation.simulate1()
    graduations = simulation.grad_prob(scenarios1)
    simulation.pp(scenarios1)
    print()
    plt.figure()
    plt.plot([i for i in range(len(graduations))], graduations, 'bo', label='Scenario 1')
    plt.ylabel('Graduation Probability')
    plt.xlabel('Probabilities %')
    plt.title('Freshman -> Graduation Chance')
    scenarios2 = simulation.simulate2()
    graduations = simulation.grad_prob(scenarios2)
    simulation.pp(scenarios2)
    print()
    plt.plot([i for i in range(len(graduations))], graduations, 'ro', label='Scenario 2')
    scenarios3 = simulation.simulate3()
    graduations = simulation.grad_prob(scenarios3)
    simulation.pp(scenarios3)
    print()
    plt.plot([i for i in range(len(graduations))], graduations, 'go', label='Scenario 3')
    plt.show()

    scenarios1 = simulation.scenario_to_q(scenarios1)
    inverses1 = simulation.i_minus_q(scenarios1)
    simulation.pp_i(inverses1)
    print()
    scenarios2 = simulation.scenario_to_q(scenarios2)
    inverses2 = simulation.i_minus_q(scenarios2)
    simulation.pp_i(inverses2)
    print()
    scenarios3 = simulation.scenario_to_q(scenarios3)
    inverses3 = simulation.i_minus_q(scenarios3)
    simulation.pp_i(inverses2)
    print()

    plt.figure()
    plt.plot([i for i in range(len(inverses1))], inverses1, 'bo', label='Scenario 1')
    plt.plot([i for i in range(len(inverses2))], inverses2, 'ro', label='Scenario 2')
    plt.plot([i for i in range(len(inverses3))], inverses3, 'go', label='Scenario 3')
    plt.xlabel('Probabilities %')
    plt.ylabel('Expected years as student')
    plt.title('Freshman Student Years Expectation')
    plt.show()
