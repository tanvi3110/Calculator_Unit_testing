import statistics as stats
import unittest
from pprint import pprint

from Statistics_module import RandomList as IntRandoms
from Statistics_module.Statistics1 import Statistics1


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics1 = Statistics1()
        self.integerRandomDataF = IntRandoms.generate_randoms(0, 30, 0, 30, False)

    def getUp(self) -> None:
        return self.integerRandomDataF

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics1, Statistics1)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics1, Statistics1)

    def test_sample_mean(self):
        self.assertEqual(self.statistics1.get_mean(self.integerRandomDataF), int(stats.mean(self.integerRandomDataF)))

    def test_sample_median(self):
        self.assertEqual(self.statistics1.get_median(self.integerRandomDataF), int(stats.median(self.integerRandomDataF)))

    if __name__ == '__main__':
        unittest.main()
