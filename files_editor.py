import logging

logging.basicConfig(filename='text.log', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s', level=logging.INFO)

print(open('/home/old-timer/PythonFiles/programs/text_for_edit.txt').read())

def edit_file(file_path):

	"""
	Accepts the path to the file as an argument.

	Reads a file by line if the current line contains a character that matches the specified variable 
	in the "choice", replaces it with the variable specified in the "change"

	Each line is written to the variable file_read.

	The final file overwrites the old without changing the name.
	"""

	file_read = ''
	choice = input('\nWhat to replace?: ')
	change = input('Enter your option: ')

	try:
		with open(file_path) as fp:
			# Scroll file line by line and replace if it necessary
			for line in fp.readlines():
				if choice in line:
					line = line.replace(choice, change)
				file_read += line

		with open(file_path, 'w+') as file_write:
			file_write.write(file_read)

		logging.info('File {} was adited'.format(file_path))
		print('File {} was adited'.format(file_path))

	except FileNotFoundError:
		print('No such file or directory: {}'.format(file_path))

if __name__ == '__main__':
	file_path = '/home/old-timer/PythonFiles/programs/text_for_edit.txt'
	edit_file(file_path)
