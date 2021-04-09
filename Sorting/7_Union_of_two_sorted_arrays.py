def Union_of_2_sorted_arrays(a,b):
    m=len(a)-1
    n=len(b)-1
    ans=[]
    i=j=0
    while (i<=m and j<=n):

        if ((i>0) and (a[i]==a[i-1])):
            i+=1
            continue
        if ((j>0) and (b[j]==b[j-1])):
            j+=1
            continue
        
        if (a[i]<b[j]):
            ans.append(a[i])
            i+=1
        elif(a[i]>b[i]):
            ans.append(b[j])
            j+=1
        else:
            ans.append(a[i])
            i+=1
            j+=1
    while (i<=m):

        if (i==0 or a[i]!=a[i-1]):
            ans.append(a[i])
        i+=1
    while (j<=n):
  
        if (j==0 or b[j]!=b[j-1]):
            ans.append(b[j])
        j+=1
        
    return ans

print(Union_of_2_sorted_arrays([1,2,3,4,5,5,6],[1,1,1,1,4,4,4,5,5,5,9,9]))
    
    
