def find_Majority(arr,n):
    res=0
    count=1
    for i in range(1,n):
        if(arr[res]==arr[i]):
            count+=1
        else:
            count-=1
        if(count==0):
            res=i
            count=1
    count=0
    for i in range(n):
        if (arr[res]==arr[i]):
            count+=1
    if (count <= n/2):
        res=-1
    return res

arr=[2,1,2,2,2,2,1,5,1]

ans=find_Majority(arr,len(arr))
if (ans==-1):
    print("No majority Element!")
else:
    print("Majority element is:",arr[ans])
