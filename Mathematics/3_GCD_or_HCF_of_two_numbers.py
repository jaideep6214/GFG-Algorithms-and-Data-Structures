'''
def gcd(a,b):
    while(a!=b):
        if (a>b):
            a=a-b
        else:
            b=b-a
    return a
'''

def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

a=int(input("Enter value for a:"))
b=int(input("Enter value for b:"))

print("GCD or HCF is :"+str(gcd(a,b)))
