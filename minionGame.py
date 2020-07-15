# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:35:35 2020

@author: MADHURIMA
"""

def miniongame(s):
    stuart=0
    kevin=0
    length=len(s)
    
    for i in range(length):
        
        if s[i] in "AEIOU":
            kevin += length-i
        else:
            stuart += length-i
            
    if kevin>stuart:
        print("Kevin",kevin)
    elif stuart>kevin:
        print("Stuart",stuart)
    else:
        print("Draw")
        

    
    
    
    
    
string=input().upper()

miniongame(string)