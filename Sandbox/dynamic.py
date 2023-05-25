def fib(n):
    arr=[0,1]
    if n>0:
        for x in range(n):
            arr.insert(x+2, arr[x]+arr[x+1])
        return arr[n-1]

print(fib(16))