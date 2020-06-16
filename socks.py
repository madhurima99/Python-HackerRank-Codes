# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 08:58:06 2020
@author: MADHURIMA
"""



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
        
    
    
