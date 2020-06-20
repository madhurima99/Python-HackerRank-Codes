# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:22:00 2020

@author: MADHURIMA
"""
from collections import Counter

def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0
    
    for v in arr:
        if v in r3:
            count += r3[v]
        
        if v in r2:
            r3[v*r] += r2[v]
        
        r2[v*r] += 1

    return count
    

n,r=[int(i) for i in input().split()]
arr=[int(i) for i in input().split()]
print(countTriplets(arr,r))
