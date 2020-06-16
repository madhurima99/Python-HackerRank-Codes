# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 08:58:06 2020

@author: MADHURIMA
"""

def compareTriplets(a, b):
    score=[0,0]
    for i in range(3):
        if a[i] > b[i]:
            score[0]+=1
        elif a[i] < b[i]:
            score[1]+=1
    
    return score
a = [int(i) for i in input("a: ").split(" ")]

b = [int(i) for i in input("b: ").split(" ")]
print(a)
print(b)
fscore=compareTriplets(a,b);
print(fscore)