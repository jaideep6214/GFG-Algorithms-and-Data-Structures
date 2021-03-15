a=[2,5,8,13,15]
b=[1,3,8,8,15,18,20,25]

n1=len(a)
n2=len(b)
i=0
j=0
while (i!=n1 and j!=n2):
    if (a[i]!=b[j]):
        if (a[i]>b[j]):
            j+=1
            try:
                while(b[j]==b[j+1]):
                    j+=1
            except:
                pass
        else:
            i+=1
            try:
                while(a[i]==a[i+1]):
                    i+=1
            except:
                pass
    else:
        print(a[i])
        i+=1
