# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:51:22 2020

@author: MADHURIMA
"""

def gradingStudents(grade) :
    newGrade=[]
    for marks in grade:
        if marks < 38:
            newGrade.append(marks)
        else:
            r = marks % 5
            nextmul5= marks-r+5
            if (nextmul5-marks) < 3 :
                newGrade.append(nextmul5)
            else:
                newGrade.append(marks)
            
        
            
    return newGrade

n=int(input())
grade=[]
for i in range (n):
    grade.append(int(input()))
    
result=gradingStudents(grade)
for marks in result:
    print(marks)