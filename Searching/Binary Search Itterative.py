arr=[1,4,5,6,9,12,25,40]
search_element=int(input("Enter element to be searched:"))
start=0
end=len(arr)-1
flag=0
while(start<=end):
    mid=int((start+end)/2)
    if arr[mid]==search_element:
        flag=1
        print("found at index:",mid)
        break
    elif(arr[mid]>search_element):
        end=mid-1
    elif(arr[mid]<search_element):
        start=mid+1
if (flag==0):
    print("Not found")
        
