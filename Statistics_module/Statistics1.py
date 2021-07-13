from Statistics_module.SampleMean import sample_mean
from Calculator.Calculator import Calculator
from Statistics_module.Median import median
from Statistics_module.Mode import mode
# from Statistics_module.Variance import stddev
from Statistics_module.Standard_Deviation import standard_deviation
from Statistics_module.Variance import variance
from Statistics_module.PopulationMean import population_mean


class Statistics1(Calculator):

    def __init__(self):
        super().__init__()

    def get_mean(self, data):
        self.result = sample_mean(data)
        return self.result

    def get_median(self, data):
        self.result = median(data)
        return self.result

    def get_mode(self, data):
        self.result = mode(data)
        return self.result

    def get_std_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result

    def get_variance(self, data):
        self.result = variance(data)
        return self.result


