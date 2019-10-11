#!/usr/bin/env python3
"""
Created on Tue Aug 15 12:07:40 2019

@author: bobo
"""

import math

#for loop
sum = 0
def div_3_5_for(start, end):
    numbers=[]
    for i in range(start, end):
        if i%3 == 0 or i%5 == 0:
            numbers.append(i)
    return numbers

print(div_3_5_for(3, 15))

# jian hua code( simplification ) 
def div_3_5_list(start, end):
    numbers_list = [i for i in range(start, end) if i%3==0 or i%5==0]
    return numbers_list
print(div_3_5_list(3, 15))

#while

def div_3_5_while(start, end):
    i = start
    number=[]
    while (i<end):
        if i%3 == 0 or i%5 == 0:
            number.append(i)
        i +=1
    return number
print(div_3_5_while(3, 15))
             

    
