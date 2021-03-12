def Bubble_sort(arr,n):
    for i in range(n):
        print("Itteration:",i+1)
        for y in range(0,n-i-1):
            if (arr[y]>arr[y+1]):
                arr[y],arr[y+1]=arr[y+1],arr[y]
        print(arr)



arr=[8,7,6,5,4,3,2,1]
print("Original Array:")
print(arr)
Bubble_sort(arr,len(arr))
