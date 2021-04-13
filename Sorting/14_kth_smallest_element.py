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

def kth_Smallest(arr,n,k):
    l=0
    r=n-1
    while(l<=r):
        print(arr)
        p=random_partition(arr,l,r)
        if (p==k-1):
            return p
        elif(p>k-1):
            r=p-1
        else:
            l=p+1
    return -1

arr=[10,4,5,8,11,6,26]
ans=kth_Smallest(arr,len(arr),k=5)
print(ans)
