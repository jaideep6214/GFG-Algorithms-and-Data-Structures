def first_element(arr,start,end,element):
    while(start<=end):
        mid=int((start+end)/2)
        if(arr[mid]==element):
            if (mid==0 or arr[mid-1]!=arr[mid]):
                return mid
            else:
                end=mid-1
        elif(arr[mid]>element):
            end=mid-1
        else:
            start=mid+1
    return -1

def end_element(arr,start,end,element):
    while(start<=end):
        mid=int((start+end)/2)
        if(arr[mid]==element):
            if (mid==len(arr)-1 or arr[mid+1]!=arr[mid]):
                return mid
            else:
                start=mid+1
        elif(arr[mid]>element):
            end=mid-1
        else:
            start=mid+1
    return -1
arr=[1,2,3,4,4,4,4,5,5,5,7,7,9,10,101,101]
start=0
end=len(arr)-1
element=int(input("Enter element:"))

f=first_element(arr,start,end,element)
if (f==-1):
    print("Number of occurance:",0)
else:
    print("Number of occurance:",end_element(arr,start,end,element)-f+1)
