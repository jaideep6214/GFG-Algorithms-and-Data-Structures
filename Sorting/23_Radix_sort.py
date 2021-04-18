def count_Sort(arr,exp):
    k=10
    n=len(arr)
    count=[]
    for i in range(0,k):
        count.append(0)
    for i in range(0,n):
        count[int((arr[i]/exp)%10)]+=1
    for i in range(1,k):
        count[i]=count[i]+count[i-1]
    output=[0 for i in range(n)]
    for i in range(n-1,-1,-1):
        output[count[int(arr[i]/exp)%10]-1]=arr[i]
        count[int(arr[i]/exp)%10]-=1
    return output
def radix_sort(arr):
    n=len(arr)
    max_element=arr[0]
    for i in range(1,n):
        if (arr[i]>max_element):
            max_element=arr[i]
    exp=1
    while (int(max_element/exp)>0):
        arr=count_Sort(arr,exp)
        exp*=10
    print(arr)

arr=[319,212,6,8,100,50]
radix_sort(arr)

