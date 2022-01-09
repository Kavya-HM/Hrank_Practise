import numpy
N,M=map(int,input().split())
array=numpy.array([input().split() for i in range(N)],int)
res1=numpy.min(array,axis=1)
print(numpy.max(res1))
