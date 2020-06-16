def sockMerchant(n,a):
    
    b=list(set(a))
    total=0;
    for i in b:
        c = a.count(i)
        pairs = int(c/2)
        total += pairs
        
    return total

n=int(input())
a=[int(i) for i in input().split(" ")][:n]
print(sockMerchant(n,a))
        
    
    