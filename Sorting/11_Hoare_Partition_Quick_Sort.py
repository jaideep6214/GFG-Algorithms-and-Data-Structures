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



def q_sort(arr,l,h):

    if (l<h):
        p=hoare_partition(arr,l,h)
        q_sort(arr,l,p)
        q_sort(arr,p+1,h)

        
arr=[6,5,1,3,10,4,2,7]

q_sort(arr,0,len(arr)-1)

print(arr)
