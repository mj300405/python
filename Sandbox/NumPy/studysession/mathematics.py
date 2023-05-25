import numpy as np

a=np.array([1,2,3,4])
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)

print(np.sin(a))

#################################

b=np.ones((2,3))
c=np.full((3,2), 2)
print(b)
print(c)
#######MATRIX MULTIPLICATION#####
d=np.matmul(b,c)
print(d)

#################################
print(np.linalg.det(d))



###########STATISTICS###############
stats=np.array([[1,2,3],[4,5,6]])
print(np.min(stats))
print(np.max(stats))
print(np.sum(stats))
print(np.sum(stats, axis=0))

#######REORGANISATION###############
before=np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after=before.reshape((4,2))
print(after)

v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
vertical=np.vstack([v1,v2,v2,v1])
horizontal=np.hstack([v2,v1,v1,v2])


print(vertical)
print(horizontal)

##########FROM_FILE###################

filedata=np.genfromtxt('data.txt', delimiter=',')
print(filedata)
filedata=filedata.astype('int32')
print(filedata) 

######ADVANCED INDEXING AND BOOLEAN MASKING #############
print(filedata>10)

ar=filedata[filedata>10]
print(ar)

print(np.any(filedata>10, axis=0))
print(np.all(filedata>10, axis=0))

print(filedata)
mat=((filedata>5)&(filedata<10))
print(mat)

#######################################################

table=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(table)

print(table[[i for i in range(4)],[i+1 for i in range(4) ]])
print(table[2:4, 0:2])
print(table[[0,4,5], 3:])
