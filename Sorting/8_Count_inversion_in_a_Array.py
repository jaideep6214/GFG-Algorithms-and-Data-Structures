def count_inversion(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    left=[]
    right=[]
    for i in range(n1):
        left.append(arr[l+i])
    for i in range(n2):
        right.append(arr[m+1+i])
    ans=i=j=0
    k=l
    while(i<n1 and j<n2):
        if (left[i]<=right[j]):
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
            ans=ans+(n1-i)
        k+=1
    while(i<n1):
        arr[k]=left[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k]=right[j]
        j+=1
        k+=1
    return ans

print(count_inversion([2,4,1,3,5],0,1,4))
