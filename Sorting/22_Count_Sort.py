def count_Sort(arr,k):
    n=len(arr)
    count=[]
    for i in range(0,k):
        count.append(0)
    for i in range(0,n):
        count[arr[i]]+=1
    for i in range(1,k):
        count[i]=count[i]+count[i-1]
    output=[0 for i in range(n)]
    for i in range(n-1,-1,-1):
        output[count[arr[i]]-1]=arr[i]
        count[arr[i]]-=1
    return output

arr=[1,4,4,1,0,1]
k=5
arr=count_Sort(arr,k)
print(arr)
    
