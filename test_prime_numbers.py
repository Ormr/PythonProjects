import unittest
from prime_numbers import primeNumber

class TestPrimeNumbers(unittest.TestCase):

	def test_primeNumber(self):
		numbers = range(1, 15)
		self.assertEqual(primeNumber(numbers), [1, 2, 3, 5, 7, 11, 13])

		numbers = [33, 37, 44, 47, 64, 99]
		self.assertEqual(primeNumber(numbers), [37, 47])

		numbers = [88]
		self.assertEqual(primeNumber(numbers), [])

		numbers = [53]
		self.assertEqual(primeNumber(numbers), [53])

if __name__ == '__main__':
	unittest.main()