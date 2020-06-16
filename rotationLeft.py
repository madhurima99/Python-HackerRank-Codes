def rotLeft(a,d):
    
    for i in range(d):
        a.append(a[0])
        a.pop(0)
        
    return a


n,d = [int(i) for i in input().split(" ")]
arr = [int(i) for i in input().split(" ")][:n]

a = rotLeft(arr,d)

for i in a:
    print(i,end=" ")