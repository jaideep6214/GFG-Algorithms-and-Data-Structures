def Selection_sort(arr,n):
    for i in range(n):
        print("Itteration:",i+1)
        min_element=arr[i]
        min_index=i
        for y in range(i+1,n):
            if (min_element>arr[y]):
                min_element=arr[y]
                min_index=y
        arr[i],arr[min_index]=arr[min_index],arr[i]
        print(arr)



arr=[8,7,6,5,4,3,2,1]
print("Original Array:")
print(arr)
Selection_sort(arr,len(arr))
