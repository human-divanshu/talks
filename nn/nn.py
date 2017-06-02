import numpy

def nonlin(x):
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


# feed forwarding
l2 = nonlin(numpy.dot(l1, w1))
l3 = nonlin(numpy.dot(l2, w2))

# error calculation
l3_errors = y - l3

print "Total error :"
print numpy.mean(numpy.abs(l3_errors))