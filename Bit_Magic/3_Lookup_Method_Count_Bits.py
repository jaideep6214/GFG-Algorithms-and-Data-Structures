table=[0 for i in range(256)]

table[0]=0
for i in range(1,256):
    table[i]=(i&1)+table[int(i/2)]

n=127
j=255
res=table[n&j]
n=n>>8
res+=table[n&j]
n=n>>8
res+=table[n&j]
n=n>>8
res+=table[n&j]

print(res)
