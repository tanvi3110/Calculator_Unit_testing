from Calculator.Calculator import Calculator
from Statistics_module.SampleMean import sample_mean


class Statistics1(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result
