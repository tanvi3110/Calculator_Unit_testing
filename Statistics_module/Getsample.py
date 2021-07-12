import random


def random_with_seed(start, stop, seed):
    random.seed(seed)
    return random.randint(start, stop)


#def getSample(data, sample_size):
#    random_values = random.sample(data, len(sample_size))
#    return random_values
