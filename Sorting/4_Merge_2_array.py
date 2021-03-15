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

arr=[2,3,5,8,34,1,6,10,40,51]
print("Original Array")
print(arr)
merge(arr,0,4,len(arr)-1)
print(arr)
