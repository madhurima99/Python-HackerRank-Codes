# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:52:18 2020

@author: MADHURIMA
"""

def freqQuery(queries):
    
    dic=dict()
    
    for sub in queries:
        if sub[0]==1:
            if sub[1] not in dic:
                dic[sub[1]]=1
            else:
                dic[sub[1]]+=1
        elif sub[0]==2:
            
            if sub[1] in dic:
               
                dic[sub[1]]-=1
                
                if sub[1]<=0:
                    del dic[sub[1]]
                
            else:
                continue
            
        elif sub[0]==3:
            if sub[1] in dic.values():
                print(1)
            else:
                print(0)
        else:
            continue
            
        

q = int(input().strip())

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

freqQuery(queries)






"""

from collections import Counter

def freqQuery(queries):
    
    freq = Counter()

    cnt = Counter()

    
    for q in queries:
        if q[0]==1:
            cnt[freq[q[1]]]-=1
            freq[q[1]]+=1
            cnt[freq[q[1]]]+=1

        elif q[0]==2:
            if freq[q[1]]>0:
                cnt[freq[q[1]]]-=1
                freq[q[1]]-=1
                cnt[freq[q[1]]]+=1

        else:
            if cnt[q[1]]>0:
                print(1)
            else:
                print(0)





            
        

q = int(input().strip())

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

freqQuery(queries)
"""