from math import factorial

def bernulli(n, k, p):
	"""
	Рахує ймовірнійсть декількох подій, котрі повторюються

	n - кількість випробувань
	k - скільки разів трапиться подія
	p - ймовірність події
	"""
	q = 1 - p # промахи
	Cnk = factorial(n)/(factorial(k) * factorial(n - k))
	P = Cnk * pow(p, k) * pow(q, n - k)
	return P * 100

if __name__ == '__main__':
	P1 = bernulli(7, 1, 1/7)
	P2 = bernulli(50, 10, 1/2)
	P3 = bernulli(3, 3, 1/6)
	P = P2 + P3
	print('P1', P1)
	print('P2', P2)
	print('P3', P3)
	print('P =', P)
