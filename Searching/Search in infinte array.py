def binarysearch(arr,start,end,element):
    while(start<=end):
        mid=int((start+end)/2)
        if(arr[mid]==element):
            return mid
        elif(arr[mid]>element):
            end=mid-1
        elif(arr[mid]<element):
            start=mid+1
    return -1
def search(arr,element):
    if (arr[0]==element):
        return 0
    i=1
    while(arr[i]<element):
        i*=2
    if(arr[i]==element):
        return i
    return binarysearch(arr,(i/2)+1,i,element)




arr=[i for i in range(0,1000000,10)]
print(arr[:10])
element=int(input("Enter element to be searched:"))

print("Index of element is :",search(arr,element))
