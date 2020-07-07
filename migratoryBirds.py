# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:58:12 2020

@author: MADHURIMA
"""

def migratoryBirds(n,arr):
    
    count=dict()
    lst=[]
    lst = [0] * 6 
    
    for i in range(len(arr)):
        
        lst[arr[i]] += 1
        
    print(lst.index(max(lst)))



n=int(input())
arr=[int(i) for i in input().split()]
migratoryBirds(n,arr)