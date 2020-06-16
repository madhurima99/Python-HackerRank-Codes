# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:05:28 2020

@author: MADHURIMA
"""
n= int(input())
def diagonalDifference(a) :
    d1=sum(a[i][i] for i in range(n))
    d2=sum(a[i][n-i-1] for i in range(n))
    return abs(d1-d2)

matrix=[]
for i in range(n):
    row=[int(i) for i in input().split(" ")][:n]
    matrix.append(row)
print(matrix)  

print("difference: ", diagonalDifference(matrix))     
        