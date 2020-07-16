# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:14:54 2020

@author: MADHURIMA
"""

def merge_the_tools(string, k):
    
    n=len(string)
    f=n//k
    for i in range(0,n,f):
        sub=[]
        if i+f < n:
            for j in string[i:i+k]:
                if j not in sub:
                    sub.append(j)
                    
        else:
            for j in string[i:i+k]:
                if j not in sub:
                    sub.append(j)
            
                
        str1=" "
        print((str1.join(sub)).replace(" ",""))

string=input()
k=int(input())
merge_the_tools(string, k)


"""
#this works

def merge_the_tools(string, k):
    
    for i in range(0, len(string), k):
        s = ""
        for j in string[i : i + k]:
            if j not in s:
                s += j          
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

"""