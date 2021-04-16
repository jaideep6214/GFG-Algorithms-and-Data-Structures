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
        
arrival=[900,940,950,1100,1500,1800]
depart=[910,1200,1120,1130,1900,2000]

q_sort(arrival,0,len(arrival)-1)
q_sort(depart,0,len(depart)-1)

i=1
j=0
res=1
curr=1
n=len(depart)
while(i<n and j<n):
    if (arrival[i]<=depart[j]):
        curr+=1
        i+=1
    else:
        curr-=1
        j+=1
    res=max(res,curr)

print(res)
