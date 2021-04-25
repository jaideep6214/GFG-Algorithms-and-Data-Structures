def power_of_two(n):
    if (n==0):
        return False
    return((n&(n-1))==0)

print(power_of_two(n=4))
print(power_of_two(n=6))
print(power_of_two(n=32))

