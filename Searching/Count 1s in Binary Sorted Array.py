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

arr=[0,0,0,0,0,0,1,1,1,1,1]
start=0
end=len(arr)-1
f=first_element(arr,start,end,1)

if(f==-1):
    print("Number of 1s are:",0)
else:
    print("Number of 1s are:",len(arr)-f)
