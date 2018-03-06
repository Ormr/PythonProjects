

def min(*args, **kwargs):
	"""
	Define minimum
	"""
	key = kwargs.get("key", None)

	def get_first_from_sorted(args, key):
		first = sorted(*args, key=key)
		return first[0]

	try:
		return get_first_from_sorted(args, key)
	
	except TypeError:
		res = sorted(args, key=key)
		return res[0]
	
def max(*args, **kwargs):

	key = kwargs.get("key", None)

	def get_first_from_sorted(args, key):
		last = sorted(*args, key=key reverse=True)
		return last[0]

	
	try:
		return get_first_from_sorted(args, key)
	
	except TypeError:
		res = sorted(args, key=key, reverse=True)
		return res[0]

"""
def get_first_from_sorted(args, key, reverse):

    if len(args) == 1:

        args = iter(args[0])

    else:

        args = iter(x for x in args)

    return sorted(args, key=key, reverse=reverse)[0]


def min(*args, **kwargs):

    key = kwargs.get("key", None)

    return get_first_from_sorted(args, key, False)



def max(*args, **kwargs):

    key = kwargs.get("key", None)

    return get_first_from_sorted(args, key, True)
"""

if __name__ == '__main__':
	print(max(2.2, 5.6, 5.9, key=int))
	print(min([3.5, 2.2, 5.6, 5.9]))
	print(max([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))
	print(min(5, 3, 7, 8, 1, 0))