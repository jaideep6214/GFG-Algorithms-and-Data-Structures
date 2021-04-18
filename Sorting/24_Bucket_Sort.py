def bucket_Sort(arr,k):
    n=len(arr)
    max_val=max(arr)
    max_val+=1
    bkt=[[]for i in range(k)]
    for i in range(n):
        bi=int(k*arr[i]/max_val)
        bkt[bi].append(arr[i])
    for i in range(k):
        bkt[i].sort()
    ans=[]
    for i in bkt:
        ans+=i
    print(ans)

arr=[30,40,10,80,5,12,70]
bucket_Sort(arr,4)
