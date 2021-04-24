'''               #Left Shift
def kthbit(n,k):
    if (n&(1<<(k-1))!=0):
        print("Yes")
    else:
        print("No")
'''
def kthbit(n,k):  #Right Shift
    if ((n>>(k-1))&1==1):
        print("Yes")
    else:
        print("No")

kthbit(n=5,k=3)
kthbit(n=5,k=2)
kthbit(n=5,k=1)
