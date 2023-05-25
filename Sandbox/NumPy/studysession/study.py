import numpy as np

array=np.genfromtxt('data1.txt', delimiter=';', dtype='int32')
print(array)

ar1=np.array(array[2:5, 2:5])
print(ar1)

ar2=np.array(array[7:,8])
print(ar2)

ar3=np.matmul(ar1,ar2)
print(ar3)

min1=np.min(array)
print(min1)

max1=np.max(array)
print(max1)

ar4=np.full_like(array, 2137)
print(ar4)

ar5=np.random.randint(21,37, size=(10,10))
print(ar5)

print([ar5>25])

ar6=ar5[ar5>25]
print(ar6)
