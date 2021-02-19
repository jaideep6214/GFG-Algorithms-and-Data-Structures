arr=[3,5,9,2,8,10,11]
arr.sort()
sum_pair=int(input("Enter sum of pairs:"))

def isPair(arr,sum_pair):
    left=0
    right=len(arr)-1
    while(left<right):
        if(arr[left]+arr[right]==sum_pair):
            print("Pair found:",arr[left]," and ",arr[right])
            return True
        elif(arr[left]+arr[right]>sum_pair):
            right-=1
        elif(arr[left]+arr[right]<sum_pair):
            left+=1
    print("Not found any pair!")
    return False

isPair(arr,sum_pair)

