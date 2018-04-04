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

<<<<<<< HEAD
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
=======
def primeNumber(args):
	"""
	The function takes a list of numbers, finds from them simple numbers and returns 
	a list of these numbers.
	
	The function has 2 loop. The first scrolls a list of numbers from the function argument, 
	the next scrolls dividers (div).

	If the number (num) is numisible by no (div), this number is difficult number.

	If number (num) is not included in the list of difficult numbers, it is a prime number.

	Parameters:
		-`prime_numbers` - list: list of prime numbers that function returns
		-`other_numbers` - list: list of the other numbers
		-`return list`
	"""
	prime_numbers = []
	other_numbers = []
	
	try:
		for num in args:
		    for div in range(2,num):
		        if num % div == 0:
		            other_numbers.append(num)
		            break
		    if num not in other_numbers:
		        prime_numbers.append(num)
	except TypeError:
		# if the arguments will be a int
		logger.exception("Tried to pass 'int' into args. It must be a list.")
	else:
		return prime_numbers
            
if __name__ == '__main__':
	numbers = list(range(100 + 1))
	prime_numbers = primeNumber(numbers)
	logger.debug("Prime numbers: {}".format(prime_numbers))
	print('\n')
	numbers = (10)
	prime_numbers = primeNumber(numbers)
	logger.debug("Prime numbers: {}".format(prime_numbers))
	
>>>>>>> 4b9f517ac0419c7198cc28b4b3f05e3f361aec25
