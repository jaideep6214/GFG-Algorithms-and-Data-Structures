def Insertion_sort(arr,n):
    for i in range(n):
        print("Itteration:",i+1)
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print(arr)



arr=[8,7,6,5,4,3,2,1]
print("Original Array:")
print(arr)
Insertion_sort(arr,len(arr))
