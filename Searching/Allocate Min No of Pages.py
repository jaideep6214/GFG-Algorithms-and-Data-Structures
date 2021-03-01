def isFeasible(arr, n, k, ans):
    req=1
    sum_all=0
    for i in range(n):
        if (sum_all +arr[i] > ans):
            req+=1
            sum_all=arr[i]
        else:
            sum_all+=arr[i]
    return req <=k

arr=[10,20,10,30]
sum_all=0
mx=0
k=2
n=len(arr)
for i in range(n):
    sum_all+=arr[i]
    mx=max(mx,arr[i])
low=mx
high=sum_all
ans=0
while(low<=high):
    mid=int((low+high)/2)
    if (isFeasible(arr,n,k,mid)):
        ans=mid
        high=mid-1
    else:
        low=mid+1

print("Each student will be allocated:",ans)
            
