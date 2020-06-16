# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:47:35 2020

@author: MADHURIMA
"""
num=int(input())

def plusMinus(a):
    p=0
    n=0
    z=0
    for i in a:
        if i<0:
            n+=1
        elif i>0:
            p+=1
        else:
            z+=1
    p = round(p/num,6)
    n = round(n/num,6)
    z = round(z/num,6)
    
    print("{:.6f}".format(p))
    print("{:.6f}".format(n))
    print("{:.6f}".format(z))
    
a=[int(i) for i in input().split(" ")][:num]
plusMinus(a)