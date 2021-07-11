from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from Statistics.SampleMean import sample_mean
from Mean import mean


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

