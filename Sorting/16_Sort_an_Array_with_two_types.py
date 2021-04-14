def seg_Positive_Negative(arr):
    n=len(arr)
    i=-1
    j=n
    while(1):
        i+=1
        while(arr[i]<0):
            i+=1
        j-=1
        while(arr[j]>=0):
            j-=1
        if (i>=j):
            return
        arr[i],arr[j]=arr[j],arr[i]

arr=[15,-3,-2,18]

seg_Positive_Negative(arr)
print(arr)
