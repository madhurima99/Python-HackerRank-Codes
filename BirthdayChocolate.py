# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:54:02 2020

@author: MADHURIMA
"""

def birthday(s,d,m):
    
    count=0
    for i in range(len(s)) :
        
        if (sum(s[ i : (i+m) ])) == d:
            
            count += 1
    
        
    print(count)
 
n=int(input())
s=[int(i) for i in input().split()][:n]
d,m=[int(i) for i in input().split()]
birthday(s,d,m)
