import numpy as np
from math import log
import math

x=np.array([0,1,2,3,4])
y=np.array([5,6,7,8,9])
z=np.add(x,y)

def myadd(x,y):
    return x+y

myadd=np.frompyfunc(myadd, 2, 1)

su=myadd(x,y)
ty=type(myadd)

con=np.concatenate((x,y), axis=0)

vs=np.vstack((x,y,z))

##################################################

a=np.add(x,y)
s=np.subtract(x,y)
m=np.multiply(x,y)
d=np.divide(x,y)
p=np.power(x,y)
r=np.remainder(x,y)#np.mod(x,y)
dm=np.divmod(x,y)
ab=np.absolute(x)

##################################################

dec=np.array([-3.142,-6.705,2.5434,9.00864])
fi=np.fix(dec)
t=np.trunc(dec)
ro=np.round(dec)
fl=np.floor(dec)
c=np.ceil(dec)

##################################################

arr=np.arange(1,11)
lg2=np.log2(arr)
lg10=np.log10(arr)
ln=np.log(arr)

nplog=np.frompyfunc(log, 2, 1)

lg100=nplog(arr, 100)

#################################################

ar1=np.array([1,2,3,4])
ar2=np.array([5,6,7,8])

ad=np.add(ar1,ar2)

su=np.sum([ar1,ar2])
su0=np.sum([ar1,ar2], axis=0)
su1=np.sum([ar1,ar2], axis=1)
cs=np.cumsum([ar1,ar2])

##################################################

pro=np.prod([ar1,ar2])
pro0=np.prod([ar1,ar2], axis=0)
pro1=np.prod([ar1,ar2], axis=1)

cp=np.cumprod([ar1,ar2])
cp0=np.cumprod([ar1,ar2], axis=0)
cp1=np.cumprod([ar1,ar2], axis=1)

###################################################

dif=np.diff([ar1,ar2])
dif0=np.diff([ar1,ar2], axis=0)
dif1=np.diff([ar1,ar2], axis=1)
dif2=np.diff([ar1,ar2], n=2)

#################################################

lc=np.lcm(14,21)
lcm=np.lcm.reduce(arr)

gc=np.gcd(8,12)
gcd=np.gcd.reduce([6,9,12,15])

##################################################

rad=np.array([np.pi/6, np.pi/2, np.pi/4, np.pi/3])
deg=np.rad2deg(rad)

val=np.array([-1,0,0.5,1, math.sqrt(3)/2])

sin=np.sin(rad)
cos=np.cos(rad)
tan=np.tan(rad)

arcsin=np.arcsin(val)
arccos=np.arccos(val)
arctan=np.arctan(val)

hypot=np.hypot(3,4)

#####################################################

sinh=np.sinh(rad)
cosh=np.cosh(rad)
tanh=np.tanh(rad)

arcsinh=np.arcsinh(val)
arccosh=np.arccosh([2,5,10])
arctanh=np.arctanh([-0.5, 0, 0.75])

#####################################################

arr=np.array([1,1,1,4,2,6,4,6,4,2])
arr1=np.array([1,2,3,4])
arr2=np.array([3,4,5,6])

arset=np.unique(arr)
uni=np.union1d(arr1,arr2)
inter=np.intersect1d(arr1, arr2, assume_unique=True)
setdiff=np.setdiff1d(arr1, arr2, assume_unique=True)
setxor=np.setxor1d(arr1, arr2, assume_unique=True)

print(setxor)