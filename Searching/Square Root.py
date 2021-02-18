def sqrt(n):
    start=1
    end=n
    ans=-1
    while(start<=end):
        mid=int((start+end)/2)
        msq=mid*mid
        if(msq==n):
            return mid
        elif(msq>n):
            end=mid-1
        elif(msq<n):
            start=mid+1
            ans=mid
    return ans

print("Sqrt of 10 is ",sqrt(10))
print("Sqrt of 9 is ",sqrt(4))
print("Sqrt of 100 is ",sqrt(100))
print("Sqrt of 109 is ",sqrt(19))

            
            
