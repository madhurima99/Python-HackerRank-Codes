# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:19:41 2020

@author: MADHURIMA
"""

def stairCase(n):
    for i in range (n):
        for j in range (n):
            if j < n-i-1 :
                print(" ",end="")
            else :
                print("#",end="")
        print()
         
n=int(input())
stairCase(n)