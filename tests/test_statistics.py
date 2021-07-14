import statistics as stats
import unittest
from Statistics_module.RandomList import RandomGenerate
from Statistics_module.Statistics1 import Statistics1


class MyTestCase(unittest.TestCase, RandomGenerate):

    def setUp(self) -> None:
        self.statistics1 = Statistics1()
        self.intRanData1 = RandomGenerate.generate_randoms(0, 30, 2, 30, True)
#        self.decRanData = RandomGenerate.generate_randoms1(10, 30, 2, 10, True)

    def getUp(self) -> None:
        return self.intRanData1
#        return self.decRanData

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics1, Statistics1)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics1, Statistics1)

    def test_sample_mean(self):
        self.assertEqual(self.statistics1.get_mean(self.intRanData1), int(stats.mean(self.intRanData1)))
 #       self.assertEqual(self.statistics1.get_mean(self.decRanData), int(stats.mean(self.decRanData)))

    def test_sample_median(self):
        self.assertEqual(self.statistics1.get_median(self.intRanData1), int(stats.median(self.intRanData1)))
 #       self.assertEqual(self.statistics1.get_median(self.decRanData), int(stats.median(self.decRanData)))

    def test_sample_mode(self):
        self.assertEqual(int(self.statistics1.get_mode(self.intRanData1)), int(stats.mode(self.intRanData1)))
#      self.assertEqual(self.statistics1.get_mode(self.decRanData), stats.mode(self.decRanData))

    def test_sample_variance(self):
        self.assertEqual(self.statistics1.get_variance(self.intRanData1), stats.variance(self.intRanData1))
 #       self.assertEqual(self.statistics1.get_variance(self.decRanData), stats.variance(self.decRanData))

    def test_sample_standard_deviation(self):
        self.assertEqual(self.statistics1.get_std_deviation(self.intRanData1), stats.stdev(self.intRanData1))
  #      self.assertEqual(self.statistics1.get_std_deviation(self.decRanData), stats.stdev(self.decRanData))

    if __name__ == '__main__':
        unittest.main()
