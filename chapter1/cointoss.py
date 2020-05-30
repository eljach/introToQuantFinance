import matplotlib.pyplot as plt
import random


class CoinToss:
    HEIGHT = 20
    WIDTH = 20

    def __init__(self, initial_value, simulations=100):
        self.initial = initial_value
        self.value = self.initial
        self.simulations = simulations

    def plot(self):
        if not hasattr(self, 'simulated_values'):
            raise Exception("No simulated values generated. Call simulate() first")
        plt.figure(figsize=(self.HEIGHT, self.WIDTH))
        plt.title("Random Walk Simulation - Coin Toss")
        plt.plot(self.simulated_values, label='Value')
        plt.show()

    def simulate(self):
        """
            Geometric random walk simulator
        """
        self.simulated_values = list()
        for i in range(self.simulations):
            if random.uniform(0,1) < 0.5:
                self.value = self.value * 0.99
            else:
                self.value = self.value * 1.01
            self.simulated_values.append(self.value)


# ins = CoinToss(100)
# ins.simulate()
# ins.plot()


