#final repeated string
def repeatedString(s,n):
    
    count_a = s.count('a')
    len_s = len(s)
    
    rep=int(n/len_s)
    
    total_count_a = rep * count_a
    
    index = n - rep * len_s
    if index != 0:
        str_left = s[:index]
        count_2 = str_left.count('a')
        total_count_a += count_2
        
        
    return total_count_a


s = input()
n = int(input())
print(repeatedString(s,n))
