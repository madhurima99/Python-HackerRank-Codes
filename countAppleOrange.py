# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:41:40 2020

@author: MADHURIMA
"""

def countAppleOrange(s,t,a,b,apples,oranges) :
      
    cnt_app=[y for y in apples if y >= s-a and y <= t-a ]
    cnt_org=[y for y in oranges if y <= t-b and y >= s-b]
    
    print(len(cnt_app))
    print(len(cnt_org))
    




s,t=[int(i) for i in input().split()]
a,b=[int(i) for i in input().split()]
m,n=[int(i) for i in input().split()]
apples=[int(i) for i in input().split()][:m]
oranges=[int(i) for i in input().split()][:n]

countAppleOrange(s,t,a,b,apples,oranges)