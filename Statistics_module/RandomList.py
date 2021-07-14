import random
import numpy as np


class RandomGenerate:
    @staticmethod
    def generate_randoms(start, stop, seed, count, duplicate):
        random.seed(seed)
        np.random.seed(seed)
        if duplicate:
            return np.random.randint(start, stop, size=count)
        else:
            return [random.randint(start, stop) for r in range(count)]

    @staticmethod
    def generate_randoms1(start, stop, seed, count, duplicate):
        random.seed(seed)
        if duplicate:
            return [random.uniform(start, stop) for i in range(count)]
        else:
            return [round(random.uniform(start, stop), 1) for i in range(count)]
