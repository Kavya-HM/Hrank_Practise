import numpy
N,M,P=map(int,input().split())
arrayN=numpy.array([input().split() for i in range(N)],int)
arrayM=numpy.array([input().split() for i in range(M)],int)
print(numpy.concatenate((arrayN,arrayM),axis=0))
