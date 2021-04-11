def naive_partition(arr, l,h,p):

    temp=[0 for i in range(h-l+1)]
    index=0
    for i in range(l,h+1):
        if (arr[i]<=arr[p]):
            temp[index]=arr[i]
            index+=1
    
    ans=index
    for i in range(l,h+1):
        if (arr[i]>arr[p]):
            temp[index]=arr[i]
            index+=1
    for i in range(l,h+1):
        arr[i]=temp[i-l]
    arr[p],arr[ans-1+l]=arr[ans-1+l],arr[p]
    return ans-1+l

def q_sort(arr,l,h):

    if (l<h):
        p=naive_partition(arr,l,h,l)
        q_sort(arr,l,p-1)
        q_sort(arr,p+1,h)

        
arr=[6,5,1,3,10,4,2,7]

q_sort(arr,0,len(arr)-1)

print(arr)
