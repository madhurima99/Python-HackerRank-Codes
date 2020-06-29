# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:53:03 2020

@author: MADHURIMA
"""

def kangaroo(x1,v1,x2,v2):
    
    if v1==v2 and x1==x2:
        return 'YES'
    elif v1==v2:
        return 'NO'
    
    x = (x2-x1) / (v1-v2)
    if( x == round(x) and x > 0):
        return 'YES'
    else:
        return 'NO'
    
x1,v1,x2,v2=[int(i) for i in input().split()]
print(kangaroo(x1,v1,x2,v2))