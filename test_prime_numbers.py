import unittest
from prime_numbers import primeNumber

class TestPrimeNumbers(unittest.TestCase):

	def test_primeNumber(self):
<<<<<<< HEAD
		numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 
		22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 
		40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 
		58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 
		77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 
		94, 95, 96, 98, 99, 100, 102, 104, 105, 106, 108, 110, 
		111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 
		123, 124, 125, 126, 128, 129, 130, 132, 133, 134, 135, 
		136, 138, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150]
		for number in numbers:
			self.assertEqual(primeNumber(number), False)

		numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
		for number in numbers:
			self.assertEqual(primeNumber(number), True)
=======
		numbers = range(1, 15)
		self.assertEqual(primeNumber(numbers), [1, 2, 3, 5, 7, 11, 13])

		numbers = [33, 37, 44, 47, 64, 99]
		self.assertEqual(primeNumber(numbers), [37, 47])

		numbers = [88]
		self.assertEqual(primeNumber(numbers), [])

		numbers = [53]
		self.assertEqual(primeNumber(numbers), [53])
>>>>>>> 4b9f517ac0419c7198cc28b4b3f05e3f361aec25

if __name__ == '__main__':
	unittest.main()