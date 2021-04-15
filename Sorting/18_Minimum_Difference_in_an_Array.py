import random
def hoare_partition(arr,l,h):
    pivot=arr[l]
    i=l-1
    j=h+1
    while (True):
        i+=1
        while (arr[i]<pivot):
            i+=1
        j-=1
        while(arr[j]>pivot):
            j-=1
        if (i>=j):
            return j
        arr[i],arr[j]=arr[j],arr[i]
def random_partition(arr,l,h):
    x=random.randint(l,h)
    arr[l],arr[x]=arr[x],arr[l]
    return hoare_partition(arr,l,h)
def q_sort(arr,l,h):
    if (l<h):
        p=random_partition(arr,l,h)
        q_sort(arr,l,p)
        q_sort(arr,p+1,h)

        
arr=[1,8,12,5,18]
q_sort(arr,0,len(arr)-1)
res=999
for i in range(1,len(arr)):
    res=min(res,arr[i]-arr[i-1])
print(res)


