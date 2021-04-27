s="abc"
n=len(s)
size=pow(2,n)
for i in range(size):
    js=str(bin(i))[2:]
    js=js[-1::-1]
    p=0
    for y in js:
        if (int(y)==1):
            print(s[p],end="")
        p+=1
    print()

    
    
