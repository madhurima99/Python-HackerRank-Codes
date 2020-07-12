# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:22:09 2020

@author: MADHURIMA MAJI
"""
def checkMagazine(magazine,note):
    
    for word in note:
        if word not in magazine:
            return "No"
        magazine.remove(word)
    
    return "Yes"
    

m,n=[int(i) for i in input().strip().split()]
magazine=[i for i in input().strip().split()]
note=[i for i in input().strip().split()]
print(checkMagazine(magazine,note))

#optimized
"""
def ransom_note(magazine, ransom):
    hash_words = {}

    # Create the hash tabled with the words on the
    # magazine and put the number of occurrence in the value.
    for m_word in magazine:
        if hash_words.get(m_word) != None:
            if (hash_words[m_word] > 0):
                hash_words[m_word] += 1
        else:
            hash_words[m_word] = 1

    # Check if exist the word in the hash table
    for r_word in ransom:
        if hash_words.get(r_word) is None or hash_words[r_word] == 0:
            return False
        else:
            hash_words[r_word] -= 1

    return True


m,n=[int(i) for i in input().strip().split()]
magazine=[i for i in input().strip().split()]
note=[i for i in input().strip().split()]
answer = ransom_note(magazine, note)

if answer:
    print ("Yes")
else:
    print ("No")
"""
