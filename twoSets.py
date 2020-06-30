# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:39:33 2020

@author: MADHURIMA
"""

def getTotalX(a,b):
    
    cf=[]
    for i in range(1,min(b)+1):
        flag=0
        for j in b:
            if j%i!=0:
                flag=1
                break
                
        if flag==0:
            cf.append(i)
            
    final=[]       
    for i in cf:
        flag=0
        for j in a:
            if i%j!=0:
                flag=1
                break
        if flag==0:
            final.append(i)
    
    print(len(final))
    



n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()][:n]
b=[int(i) for i in input().split()][:m]
getTotalX(a,b)