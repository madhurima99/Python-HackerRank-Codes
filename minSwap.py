def minSwap(a):
    swap=0
    for i in range(len(a)-1):
        min1=min(a[i+1:])
        j=a.index(min1)
        if(a[i] > min1):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            swap += 1
            
    return swap

n = int(input())
arr = [int(i) for i in input().split(" ")][:n]
print(minSwap(arr))
         

"""
def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps
            
    return swap

n = int(input())
arr = [int(i) for i in input().split(" ")][:n]
print(minimumSwaps(arr))

"""