def power (x,n):
    res=1
    while(n>0):
        if (n%2!=0):
            res=res*x
        x=x*x
        n=int(n/2)
    return res

print(power(2,10))
