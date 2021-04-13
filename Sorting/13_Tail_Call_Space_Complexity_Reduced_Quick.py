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

    while (l<h):
        p=random_partition(arr,l,h)
        if (p-l <h-p):
            q_sort(arr,l,p)
            l=p+1
        else:
            q_sort(arr,p+1,h)
            h=p-1


        
arr=[6,5,1,3,10,4,2,7]

q_sort(arr,0,len(arr)-1)

print(arr)
