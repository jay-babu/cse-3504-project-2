from random import choice
from matplotlib import pyplot as plt


class Problem3:

    def __init__(self):
        # self.graph = [1, 2, 3, 4, 5, 6]
        self.vertex = 1
        self.time = 0
        self.graph = {1: [2], 2: [3, 4], 3: [5], 4: [3, 3, 3, 6], 5: [4, 6, 2, 2]}
        self.avg_visits = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1}

    def reset(self):
        self.vertex = 1
        self.time = 0
        self.avg_visits = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1}

    def walk(self):
        self.reset()
        while self.vertex != 6:
            self.time += 2 * self.vertex + 1
            self.avg_visits[self.vertex] += 1
            self.vertex = choice(self.graph.get(self.vertex))
        return self.time

    def c(self):
        execution_times = []
        for p23 in range(1, 10):
            p2 = []
            for _ in range(p23):
                p2.append(3)
            for _ in range(10 - p23):
                p2.append(4)
            self.graph[2] = p2
            execution_times.append((p23 / 10, self.walk()))

        plt.figure()
        plt.plot([percentage for percentage, _ in execution_times], [time for _, time in execution_times], label='p23')
        plt.xlabel('p23 percentage chance')
        plt.ylabel('Execution times')
        plt.show()
        return execution_times


if __name__ == '__main__':
    simulation = Problem3()
    simulation.walk()
    print(simulation.time)
    print(simulation.avg_visits)
    print(simulation.c())
