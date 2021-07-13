import statistics as stats
import unittest
from pprint import pprint

from Statistics_module import RandomList as IntRandoms
from Statistics_module.Statistics1 import Statistics1


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics1 = Statistics1()
        self.integerRandomDataT = IntRandoms.generate_randoms(0, 30, 2, 30, True)

    def getUp(self) -> None:
        return self.integerRandomDataT

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics1, Statistics1)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics1, Statistics1)

    def test_sample_mean(self):
        self.assertEqual(self.statistics1.get_mean(self.integerRandomDataT), int(stats.mean(self.integerRandomDataT)))

    def test_sample_median(self):
        self.assertEqual(self.statistics1.get_median(self.integerRandomDataT), int(stats.median(self.integerRandomDataT)))

    def test_sample_mode(self):
        self.assertEqual(int(self.statistics1.get_mode(self.integerRandomDataT)), int(stats.mode(self.integerRandomDataT)))

    if __name__ == '__main__':
        unittest.main()
