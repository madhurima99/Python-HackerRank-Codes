# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 00:20:30 2020

@author: MADHURIMA
"""

"""def arrayManipulation(n,queries):
    a=[0]*(n+1)
    a=a[1:]
    for i in queries:
        for j in range(i[0],(i[1]+1)):
            a[j-1] += i[2]
        
    return max(a)
        
        
n,m=[int(i) for i in input().split(" ")]
queries=[]
for i in range(m):
    sub=[int(i) for i in input().split(" ")][:3]
    queries.append(sub)
    
print(arrayManipulation(n,queries))"""



"""n,m=[int(i) for i in input().split(" ")]
arr=[0]*(n)

for i in range(m):
    a,b,k=[int(p) for p in input().split(" ")]
    
    for j in range(a,b+1):
        arr[j-1] += k
    
    
    
print(max(arr))"""

#final
#difference and prefix array
n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr;
max = x = 0
for i in list:
   x=x+i;
   if(max<x): max=x;
print(max)
