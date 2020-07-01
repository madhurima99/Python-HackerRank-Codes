# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:17:28 2020

@author: MADHURIMA
"""
def breakingRecords(scores) :
    
    min1=scores[0]
    max1=scores[0]
    count_min=0
    count_max=0
    
    for i in scores:
        
        if i < min1:
            min1 = i
            count_min += 1
            continue
        
        if i > max1:
            max1 = i
            count_max += 1
            
    print(count_max,count_min)


n=int(input())
scores=[int(i) for i in input().split()]
breakingRecords(scores)