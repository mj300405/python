import numpy as np

#SHAPE1
shape=np.full((10,10), 1)
shape[1:9,1:9]=0
shape[[i for i in range(10)],[i for i in range(10)]]=1
shape[[i for i in reversed(range(10))],[i for i in range(10)]]=1
shape[4:6,]=6
shape[:,4:6]=6
shape[4:6,4:6]=8

print(shape)
print('\n\n\n')


#SHAPE2
shape=np.zeros((10,10), dtype='int16')
for i in range(10):
    shape[[i],[j for j in range(i%2,10,2)]]=1

print(shape)
print('\n\n\n')



#SHAPE3
shape=np.zeros((10,10),dtype='int8')
shape[0:10:2,0:10:2]=1

print(shape)
print('\n\n\n')

#SHAPE4
shape=np.zeros((10,10), dtype='int8')
for i in range(5):
    shape[i:10-i,i:10-i]=(i+1)%2

print(shape)
print('\n\n\n')