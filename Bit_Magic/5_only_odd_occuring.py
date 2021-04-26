def find_odd(arr):
    res=0
    for i in arr:
        res=res^i
    return res

arr=[1,1,2,3,2,2,4,2,3,4,3]

print(find_odd(arr))
