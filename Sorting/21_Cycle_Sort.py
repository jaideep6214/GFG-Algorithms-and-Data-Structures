def cycle_sort(arr):  #Distinct elements
    n=len(arr)
    for cs in range(0,n-1):
        item=arr[cs]
        pos=cs
        for i in range(cs+1,n):
            if (arr[i]<item):
                pos+=1
        item,arr[pos]=arr[pos],item
        while(pos!=cs):
            pos=cs
            for i in range(cs+1,n):
                if (arr[i]<item):
                    pos+=1
            item,arr[pos]=arr[pos],item

arr=[20,50,40,10,30]
cycle_sort(arr)
print(arr)
