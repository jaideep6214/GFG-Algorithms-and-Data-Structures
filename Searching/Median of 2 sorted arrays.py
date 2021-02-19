arr1=[5,6,7,8]
arr2=[30,40,50,60]

def getMed(arr1,arr2,n1,n2):
    begin=0
    end=n1
    while(begin<=end):
        i1=int((begin+end)/2);
        i2=int((n1+n2+1)/2)-i1
        if(i1==n1):
            min1=999
        else:
            min1=arr1[i1]

        if(i1==0):
            max1=-999
        else:
            max1=arr1[i1-1]

        if(i2==n2):
            min2=999
        else:
            min2=arr2[i2]

        if(i2==0):
            max2=-999
        else:
            max2=arr2[i2-1]

        if(max1 <= min2 and max2 <= min1):
            if((n1+n2)%2==0):
                return (max(max1,max2)+min(min1,min2))/2
            else:
                return max(max1,max2)
        elif(max1>min2):
            end=i1-1
        else:
            begin=i1+1
if (len(arr1)>len(arr2)):
    arr1,arr2=arr2,arr1
print(arr1,arr2)
print("Median of combined array is :",getMed(arr1,arr2,len(arr1),len(arr2)))
    
