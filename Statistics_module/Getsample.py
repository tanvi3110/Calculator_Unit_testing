import random


class RandomSeed:
    @staticmethod
    def random_with_seed(start, stop, seed):
        random.seed(seed)
        return random.randint(start, stop)

    @staticmethod
    def random_with_seed1(start, stop, seed):
        random.seed(seed)
        return random.uniform(start, stop)

    @staticmethod
    def random_without_seed(start, stop):
        return random.uniform(start, stop)

    @staticmethod
    def random_without_seed1(start, stop):
        return random.uniform(start, stop)
