# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:15:18 2020

@author: MADHURIMA
"""

def countSwaps(a):
    print(a)
    swap=0
    for i in range (len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                print(a)
                swap +=1
    print("Array is sorted in", swap,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
    
n=int(input())
arr=[int(i) for i in input().split()][:n]
countSwaps(arr)