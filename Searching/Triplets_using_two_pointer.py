arr=[3,5,9,2,8,10,11]
arr.sort()
sum_triples=int(input("Enter sum of triplets:"))

def isPair(arr,sum_triples):
    left=0
    right=len(arr)-1
    while(left<right):
        if(arr[left]+arr[right]==sum_triples):
            print("Triplets found:",arr[left]," and ",arr[right]," and ",end="")
            return True
        elif(arr[left]+arr[right]>sum_triples):
            right-=1
        elif(arr[left]+arr[right]<sum_triples):
            left+=1
    return False
flag=0
for i in range(len(arr)):
    if(isPair(arr[i+1:],sum_triples-arr[i])):
        flag=1
        print(arr[i])
if (flag==0):
    print("Not found any pair!")
