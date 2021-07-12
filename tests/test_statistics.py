import statistics
import unittest
from random import randint
from random import seed
from Statistics_module.Statistics1 import Statistics1
from Statistics_module.Mean import mean
from Statistics_module.Getsample import getSample


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        seed(5)
        self.statistics = Statistics1()
        self.testData = float(randint(0, 10))

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics1)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics1)

    def test_sample_mean(self):
        self.assertEqual(self.statistics.result, statistics.mean(self.testData))
       # self.assertEqual(self.statistics.result, statistics.mean(self.testData))


if __name__ == '__main__':
    unittest.main()
