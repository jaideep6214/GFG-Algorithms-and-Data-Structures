import random

def lomuto_partition(arr,l,h):
    pivot=arr[h]
    i=l-1

    for j in range(l,h):
        if (arr[j]<pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[h],arr[i+1]=arr[i+1],arr[h]
    return i+1   



def random_partition(arr,l,h):
    x=random.randint(l,h)
    arr[l],arr[x]=arr[x],arr[l]
    return lomuto_partition(arr,l,h)

def kth_Smallest(arr,n,k):
    l=0
    r=n-1
    while(l<=r):
        p=random_partition(arr,l,r)
        print (arr,p)
        if (p==k-1):
            return p
        elif(p>k-1):
            r=p-1
        else:
            l=p+1
    return -1

arr=[10,4,5,8,11,6,26]
ans=kth_Smallest(arr,len(arr),k=5)
print(arr[ans]," is the element");
