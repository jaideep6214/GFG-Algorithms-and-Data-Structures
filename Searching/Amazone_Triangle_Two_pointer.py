arr=[3,5,6,4,8,10,11]
arr.sort()

def isTriangle(arr,c):
    left=0
    right=len(arr)-1
    while(left<right):
        if(pow(arr[left],2)+pow(arr[right],2)==pow(c,2)):
            print("Tringle found:",arr[left]," and ",arr[right]," and ",end="")
            return True
        elif(pow(arr[left],2)+pow(arr[right],2)>pow(c,2)):
            right-=1
        elif(pow(arr[left],2)+pow(arr[right],2)<pow(c,2)):
            left+=1
    return False
flag=0
for i in range(len(arr)-1,-1,-1):
    if(isTriangle(arr[:i],arr[i])):
        flag=1
        print(arr[i])
if (flag==0):
    print("Not found any Triangles!")
