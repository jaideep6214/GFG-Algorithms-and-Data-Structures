def Binary_search(arr,start,end,search_element):
    if(start<=end):
        mid=int((start+end)/2)
        if arr[mid]==search_element:
            return (mid)
        elif(arr[mid]>search_element):
            return Binary_search(arr,start,mid-1,search_element)
        elif(arr[mid]<search_element):
            return Binary_search(arr,mid+1,end,search_element)
    else:
        return(-1)

arr=[1,4,5,6,9,12,25,40]
search_element=int(input("Enter element to be searched:"))
start=0
end=len(arr)-1
ans=Binary_search(arr,start,end,search_element)
if (ans==-1):
    print("Not found")
else:
    print("Found at index ",ans)
        
