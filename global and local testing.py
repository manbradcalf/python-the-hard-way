x = 6

def example():

	globx = x
	print(globx)
	globx+=5
	print(globx)
	return globx

example()

x = example()

print x