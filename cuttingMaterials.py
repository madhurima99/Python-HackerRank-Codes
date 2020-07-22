"""Cutting a material
Max. score: 100
You are given a disk-shaped or circular material. Determine the maximum number of pieces in which the material can be cut into by using exactly  straight cuts.

You must perform the task for  tasks separately.

Input format

The first line contains  denoting the number of test cases.
Next  lines contain a single integer .
Output format

Print  separate lines each containing answer for each test case.

Note: Use a 64-bit variable to store and read all the variables."""

t=int(input())
cuts=[]
for i in range(t):
    n=int(input())
    p = int((n**2 + n + 2)/2)
    cuts.append(p)

for i in cuts:
    print(i)


