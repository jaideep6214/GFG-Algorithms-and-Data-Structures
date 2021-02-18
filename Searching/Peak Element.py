def get_A_peak (arr):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=int((start+end)/2)
        if((mid==0 or arr[mid-1]<=arr[mid]) and (mid==len(arr)-1 or arr[mid+1]<=arr[mid])):
            return arr[mid]
        if(mid>0 and arr[mid-1]>=arr[mid]):
            end=mid-1
        else:
            start=mid+1
    return -1

arr=[5,20,40,30,20,50,60]
print("Peak is:",get_A_peak(arr))

arr=[550,50,40,30,20,50,60]
print("Peak is:",get_A_peak(arr))
