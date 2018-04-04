import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('prime_debug.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_heandler = logging.StreamHandler()
# stream_heandler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_heandler)

def primeNumber(num):
	"""
	Check if num is a prime number - return True
	else return False
	"""
	res = True
	try:
		for div in range(2, num):
			if num % div == 0:
				res = False
				break
		# print(num, '\t->', res)
		return res
	except TypeError:
		logger.exception("Incorrect arg. It must be a int.")

if __name__ == '__main__':
	number = 3
	prime_number = primeNumber(number)
	logger.debug("Prime number: {}".format(prime_number))
