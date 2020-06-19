# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:54:00 2020

@author: MADHURIMA
"""

def twoStrings(s1,s2):
    
    if len(s1) < len(s2):
        small=s1
        big=s2
    else:
        small=s2
        big=s1
        
    for i in small:
        if i in big:
            return "YES"
    
    return "NO"
    

result=[]
p=int(input())
for _ in range(p):
    s1=input()
    s2=input()
    result.append(twoStrings(s1,s2))
    
for i in result:
    print(i)