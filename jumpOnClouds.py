def jumpingOnClouds(c):
    
    i=0
    jump=0   
    while(i < len(c)-1):
        if i + 2 >= n or c[i + 2] == 1:   # Not possible to make a jump of size 2
            i = i + 1
            jump = jump + 1
        else:
            i = i + 2
            jump = jump + 1
            
    return jump
 
n=int(input())
c=[int(i) for i in input().split(" ")][:n]
print(jumpingOnClouds(c))

