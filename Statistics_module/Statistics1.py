from Statistics_module.SampleMean import sample_mean
from Calculator.Calculator import Calculator
from Statistics_module.Median import median
from Statistics_module.Mode import mode
from Statistics_module.Standard_deviation import stddev
from Statistics_module.Variance import variance
from Statistics_module.PopulationMean import population_mean


class Statistics1(Calculator):
#    data = []

    def __init__(self):
        super().__init__()

    def get_mean(self, data):
        self.result = sample_mean(data)
        return self.result

    def population_mean(self, data):
        self.result = population_mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def stddev(self, data):
        self.result = stddev(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result
