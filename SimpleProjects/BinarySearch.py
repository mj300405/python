import random

def binarySearch(table, value, low=None, high=None):
    if low is None:
        low=0
    if high is None:
        high = len(table)-1
    if high<low:
        return -1

    mid=(low+high)//2

    if table[mid]==value:
        return mid
    elif value<table[mid]:
        return binarySearch(table, value, low, mid-1)
    else:
        return binarySearch(table, value, mid+1, high)
    


