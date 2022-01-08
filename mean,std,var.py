import numpy
N, M = map(int, input().strip().split())
array=numpy.array([input().strip().split() for _ in range(N) ], int)
print(numpy.mean(array, axis = 1))
print(numpy.var(array, axis = 0))
print(round(numpy.std(array, axis = None),11))
