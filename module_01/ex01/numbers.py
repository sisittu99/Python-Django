def numbers():

	# we have to open the file in read mode
	with open('numbers.txt', 'r') as f:
		data = f.read()
		data = data.split(',')
		data = [int(i) for i in data]
		for x in data:
			print(x)

if __name__ == '__main__':
	numbers()
