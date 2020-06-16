#hourglass sum in a 6x6 matrix

def hourglassSum(m,i,j):
    
    sum1 = m[i-1][j-1] + m[i-1][j] + m[i-1][j+1] + m[i][j] + m[i+1][j-1] + m[i+1][j] + m[i+1][j+1]
    
    return sum1


matrix=[]
for i in range(6):
    
    row=[int(i) for i in input().split(" ")][:6]
    
    matrix.append(row)

    
max_hourglass_sum=-63 #constraints
for i in range(1,5):
    
    for j in range(1,5):
        
        current_hourglass_sum = hourglassSum(matrix,i,j)
        
        if current_hourglass_sum > max_hourglass_sum :
            max_hourglass_sum = current_hourglass_sum
            

print(max_hourglass_sum)