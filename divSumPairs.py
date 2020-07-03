# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:54:38 2020

@author: MADHURIMA
"""

def divSumPairs(n,k,ar):
    
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    print(count)



n,k=[int(i) for i in input().split()]
ar=[int(i) for i in input().split()][:n]
divSumPairs(n,k,ar)