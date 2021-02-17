arr=[10,10,10,20,20,20,30,30,40,50,60,60,60]
search_element=int(input("Enter element to be searched:"))
start=0
end=len(arr)-1
flag=0
while(start<=end):
    mid=int((start+end)/2)
    if(arr[mid]==search_element):
        if (mid==0 or arr[mid-1]!=arr[mid]):
            flag=1
            print("Found at index ",mid)
            break
        else:
            end=mid-1
    elif(arr[mid]>search_element):
        end=mid-1
    elif(arr[mid]<search_element):
        start=mid+1
if(flag==0):
    print("Not found!")
        
