import unittest
from random import randint
from random import seed
from Statistics.Statistics import Statistics
from Statistics.Mean import mean


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 10)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 4.25)


if __name__ == '__main__':
    unittest.main()
