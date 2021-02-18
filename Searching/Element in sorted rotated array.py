def search (arr,element):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=int((start+end)/2)
        if(arr[mid]==element):
            return mid
        if(arr[start]<arr[mid]):
            if(element>=arr[start] and element < arr[mid]):
                end=mid-1
            else:
                start=mid+1
        else:
            if(element>arr[mid] and element <= arr[end]):
                start=mid+1
            else:
                end=mid-1
    return -1

arr=[50,60,70,80,90,100,110,120,20,30,40]
element=int(input("Enter element to be searched:"))
print("Index of element in:",search(arr,element))
