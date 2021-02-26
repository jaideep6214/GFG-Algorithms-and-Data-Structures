def find_Repeat(arr,n):
    slow=arr[0]
    fast=arr[0]
    flag=0
    while(slow!=fast or flag==0):
        flag=1
        slow=arr[slow]+1
        fast=arr[arr[fast]+1]+1

    slow=arr[0]
    while(slow!=fast):
        slow=arr[slow]+1
        fast=arr[fast]+1

    return slow-1

arr=[0,1,2,3,4,5,1]

print("Repeating element is :",arr[find_Repeat(arr,len(arr))])
