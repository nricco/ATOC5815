#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 07:21:29 2020

@author: zhwa2432
"""


import array as arr
a = arr.array('i', [2, 4, 6, 8])

print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])

#Slicing Python Arrays

numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5]) # 3rd to 5th
print(numbers_array[:-5]) # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])   # beginning to end

# Changing and Adding Elements

numbers = arr.array('i', [1, 2, 3, 5, 7, 10])

# changing first element
numbers[0] = 0    
print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])

# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])   
print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])

print()
numbers = arr.array('i', [1, 2, 3, 5, 7, 10]) 
# changing first element 
numbers[0] = 0 
print(numbers)
# changing 3rd to 5th element 
numbers[2:5] = arr.array('i', [4, 6, 8]) 
print(numbers)

print()
numbers = arr.array('i', [1, 2, 3]) 
numbers.append(4)
print(numbers)
# extend() appends iterable to the end of the array 
numbers.extend([5, 6, 7]) 
print(numbers)


print()
odd = arr.array('i', [1, 3, 5]) 
even = arr.array('i', [2, 4, 6]) 
numbers = arr.array('i') # creating empty array of integer 
numbers = odd + even 
print(numbers)
