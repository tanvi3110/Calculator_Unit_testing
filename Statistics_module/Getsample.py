import random
import numpy as np


def generate_randoms(start, end, seed, count):
    np.random.seed(seed)
    return np.random.randint(start, end, size=count)


def random_with_seed(start, end, seed):
    random.seed(seed)
    return random.randint(start, end)
