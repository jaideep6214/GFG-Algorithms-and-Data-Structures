def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return((a*b)/gcd(a,b))

a=int(input("Enter value for a:"))
b=int(input("Enter value for b:"))

print("LCM is :"+str(int(lcm(a,b))))
