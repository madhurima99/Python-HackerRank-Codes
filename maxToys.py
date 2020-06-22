# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:20:33 2020

@author: MADHURIMA
"""

def maximumToys(prices,k) :
    prices=sorted(prices)
    item=0
    maxprice=0
    for p in prices:
        maxprice += p
        if maxprice < k:
            item += 1
            
    return item;

n,k = [int(i) for i in input().split()]
prices= [int(i) for i in input().split()] 
print(maximumToys(prices,k))
             
         
         
     