# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the circularArrayRotation function below.
# def circularArrayRotation(a, k, queries):
#     rot=0
#     for i in range(len(a)):
#         if rot<k:
#             a.insert(0,a[-1])
#             a.pop()
#             rot += 1
#     for q in queries:
#         print(a[q])


        
# if __name__ == '__main__':
    

#     nkq = input().split()

#     n = int(nkq[0])

#     k = int(nkq[1])

#     q = int(nkq[2])

#     a = list(map(int, input().rstrip().split()))

#     queries = []

#     for _ in range(q):
#         queries_item = int(input())
#         queries.append(queries_item)

#     circularArrayRotation(a, k, queries)

    
n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
k=k%n
arr=arr[-k:]+arr[:-k]
for i in range(q):
    X=int(input())
    print(arr[X])
    
