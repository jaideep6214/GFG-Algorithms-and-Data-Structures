import random
def hoare_partition(arr,l,h):
    pivot=arr[l][0]
    i=l-1
    j=h+1
    while (True):
        i+=1
        while (arr[i][0]<pivot):
            i+=1
        j-=1
        while(arr[j][0]>pivot):
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

        
arr=[[1,3],[2,4],[5,7],[6,8]]
q_sort(arr,0,len(arr)-1)
res=0
for i in range(1,len(arr)):
    if (arr[res][1]>=arr[i][0]):
        arr[res][0]=min(arr[res][0],arr[i][0])
        arr[res][1]=max(arr[res][1],arr[i][1])
        print(arr[res], end="")
    else:
        res+=1
        arr[res]=arr[i]
    
       




