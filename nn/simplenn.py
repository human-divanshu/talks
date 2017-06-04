import numpy

def nonlin(x, deriv=False):
	if deriv == True:
		return (x * (1 - x))
	return (1/(1 + numpy.exp(-x)))


# input data
# This data represents an NAND gate
# each value is array of 1 x 2
x = numpy.array([[0,0],
				 [0,1],
				 [1,0],
				 [1,1]])

# corresponding output for input data
# This represents output of NAND gate
y = numpy.array([[1],
				[1],
				[1],
				[0]])

# input layer is matrix of 1 (input nodes) x 2 (no. of nodes in this layer) i.e 1 x 2
l1 = x
# w1 should be 2 (input nodes) x (no. of nodes in this layer) i.e 2 x 4
w1 = numpy.random.rand(2, 4) + 1
# w2 should be (input nodes) x (no of nodes in this layer) i.e 4 x 1
w2 = numpy.random.rand(4, 1) + 1

epochs = 500

# training
for e in range(epochs):

	# feed forwarding
	l2 = nonlin(numpy.dot(x, w1))
	l3 = nonlin(numpy.dot(l2, w2))

	# error and back propagation
	l3_errors = y - l3

	if (e % 10000) == 0:
		total_error = numpy.mean(numpy.abs(l3_errors))
		print "Output error : " + str(total_error)
	
	l3_delta = l3_errors * nonlin(l3, deriv=True)

	l2_error = l3_delta.dot(w2.T)

	l2_delta = l2_error * nonlin(l2, deriv=True)

	w2 += l2.T.dot(l3_delta)
	w1 += l1.T.dot(l2_delta)

print l3


def query(x, y):
	global w1, w2
	input_data = numpy.array([x,y], dtype=int)
	l2 = nonlin(numpy.dot(input_data, w1))
	l3 = nonlin(numpy.dot(l2, w2))

	return l3


run = True

while run:
	print "Enter value of x and y (seperated by space) or q to quit"
	res = raw_input().strip()
	if res == "q":
		run = False
		continue
	else:
		l = res.split(' ')
		ans = query(l[0], l[1])
		if ans > 0.5:
			print 1
		else:
			print 0
