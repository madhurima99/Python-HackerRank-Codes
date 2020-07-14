# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:02:41 2020

@author: MADHURIMA
"""

"""from statistics import median

def activityNotification(lst,d):
    alert=0
    for i in range(len(lst)):
        indx=i+d
        if indx < len(lst):
            med=median(lst[i:i+d])
            if(lst[i+d] >= med*2):
                alert += 1
                
        else:
            break
        
    
    print(alert)
    
n,d=[int(i) for i in input().split()]
lst=[int(i) for i in input().split()][:n]

activityNotification(lst,d) """

import bisect
n,d=map(int,input().split())
exp=list(map(int,input().split()))
arr=sorted(exp[:d])
m=d//2
c=0
def med(arr,d,m):
    if d % 2 == 0:
        return sum(arr[m - 1:m + 1]) / 2
    else :
        return arr[int(m)]    
for i in range(d,n):
    if exp[i] >= 2*med(arr,d,m):        
        c+=1
    del arr[bisect.bisect_left(arr,exp[i-d])]
    bisect.insort(arr,exp[i])
print(c)   


 