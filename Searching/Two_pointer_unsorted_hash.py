arr=[3,5,9,2,8,10,11]

sum_pair=int(input("Enter sum of pairs:"))
d={}
flag=0
for e in arr:
    if (sum_pair-e in d):
        flag=1
        print("Pair found:",e," and ",sum_pair-e)
    else:
        d[e]=1
if(flag==0):
    print("Not found any pair!")
