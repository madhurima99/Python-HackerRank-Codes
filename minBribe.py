# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 09:22:06 2020
@author: MADHURIMA
"""

def minBribe(q):
    
    counter = 0
    for i in range(len(q)):
        if q[i]-(i+1) > 2:
            print("Too chaotic")
            return
        
        for j in range(max(0,q[i]-2),i):
            if q[j] > q[i]:
                counter += 1
    print(counter)
    
t = int(input())
for i in range(t):
    n = int(input())
    q = list(map(int, input().rstrip().split()))
    minBribe(q)
