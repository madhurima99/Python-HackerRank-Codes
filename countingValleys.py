# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 09:22:06 2020
@author: MADHURIMA
"""

def countingValleys(n,steps):
    
    valley = seaLevel = 0
    
    for step in steps:
        
        if step=='U':
            seaLevel += 1
        else:
            seaLevel -= 1
            
        if step=='U' and seaLevel==0:
            valley += 1
    
    return valley

n = int(input())
steps = input()
print(countingValleys(n,steps))
        
   
