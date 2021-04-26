def two_odd_appearing(arr,n):
    xor=0
    res1=0
    res2=0
    for i in range(n):
        xor=xor^arr[i]
    right_set_bit=(xor&(~(xor-1)))
    for i in range(n):
        if ((arr[i]&right_set_bit)!=0):
            res1=res1^arr[i]
        else:
            res2=res2^arr[i]
    print(res1,res2)

arr=[3,4,3,4,5,4,4,6,7,7]
two_odd_appearing(arr,len(arr))
