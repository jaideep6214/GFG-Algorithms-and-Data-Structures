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

        
arr=[6,5,1,3,10,4,2,7]
n=len(arr)
m=3
if (m>n):
    print(-1)
    
q_sort(arr,0,n-1)

res=arr[m-1]-arr[0]
for i in range(1,n-m+1):
    res=min(res,(arr[i+m-1]-arr[i]))

print(res)
