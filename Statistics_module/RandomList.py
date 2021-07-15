import random
import numpy as np


class RandomGenerate:
    @staticmethod
    def generate_random_integer(start, stop, seed, count, duplicate):
        random.seed(seed)
        np.random.seed(seed)
        if duplicate:
            return np.random.randint(start, stop, size=count)
        else:
            return [random.randint(start, stop) for r in range(count)]

    @staticmethod
    def generate_random_decimal(start, stop, seed, count, duplicate):
        random.seed(seed)
        if duplicate:
            return [random.uniform(start, stop) for i in range(count)]
        else:
            return [round(random.uniform(start, stop), 1) for i in range(count)]

    @staticmethod
    def generate_random_integer_no_seed(r1, r2):
        random_list = []
        for i in range(r1, r2):
            random_list = random.randint(r1, r2)
        return random_list

    @staticmethod
    def generate_random_decimal_no_seed(r1, r2):
        random_list1 = []
        for i in range(r1, r2):
            random_list1 = random.randint(r1, r2)
        return random_list1

