def lomuto_partition(arr,l,h):
    pivot=arr[h]
    i=l-1

    for j in range(l,h):
        if (arr[j]<pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[h],arr[i+1]=arr[i+1],arr[h]
    return i+1   



def q_sort(arr,l,h):

    if (l<h):
        p=lomuto_partition(arr,l,h)
        q_sort(arr,l,p-1)
        q_sort(arr,p+1,h)

        
arr=[6,5,1,3,10,4,2,7]

q_sort(arr,0,len(arr)-1)

print(arr)
