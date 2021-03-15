def merge(arr,l,m,h):
    n1=m-l+1
    n2=h-m
    left=[]
    right=[]

    for i in range(n1):
        left.append(arr[l+i])
    for j in range(n2):
        right.append(arr[m+1+j])
 
    i=0
    j=0
    k=l
    while(i<n1 and j<n2):
        if (left[i]<=right[j]):
            arr[k]=left[i]
            k+=1
            i+=1
        else:
            arr[k]=right[j]
            k+=1
            j+=1
    while(i<n1):
        arr[k]=left[i]
        k+=1
        i+=1
    while(i<n2):
        arr[k]=right[j]
        k+=1
        j+=1
def mergesort(arr,l,r):
    if (r>l):
        m=int((l+r)/2)
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)

arr=[10,9,8,7,6,5,4,3,2,1]

mergesort(arr,0,len(arr)-1)

print(arr)
        
