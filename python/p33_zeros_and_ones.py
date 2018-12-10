import numpy

# Solution 1
# d = input().replace(' ', ',')

# print(numpy.zeros((eval(d)), dtype=numpy.int))
# print(numpy.ones((eval(d)), dtype=numpy.int))

# Solution 2
d = tuple(map(int, input().split()))

print(numpy.zeros(d, dtype=numpy.int))
print(numpy.ones(d, dtype=numpy.int))

