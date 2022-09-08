#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:03:25 2020

@author: zhwa2432
"""


# a file named "geek", will be opened with the reading mode. 
file = open('geek.txt', 'r') 
# This will print every line one by one in the file 
# for each in file: 
#    print (each) 
print(file.read())
file.close()     

print()

# Python code to create a file 
file = open('geek_2.txt','w') 
file.write("This is the write command\n") 
file.write("It allows us to write in a particular file\n") 
file.close() 

# Python code to illustrate read() mode character wise 
file = open("geek_2.txt", "r") 
print(file.read())
print(file.read(5)) 


# Python code to illustrate append() mode 
file = open('geek_2.txt','a') 
file.write("This will add this line") 
file.close() 

file = open("geek_2.txt", "r") 
print(file.read())
file.close() 

print('\n read:')
# Python code to illustrate with() 
with open("geek_2.txt") as file:   
    data = file.read()  
# do something with data 
    data=list(data)
    print(type(data))
    print(data)

    for line in data: 
        word = line.split() 
        print('word',word) 
    
    
print('\n readlines():')
    
# Python code to illustrate split() function 
with open("geek_2.txt", "r") as file: 
    #data = file.readlines() 
    data = file.readline(100) 
    print(type(data))
    print(data)
    for line in data: 
        word = line.split() 
        print('word',word)
        
file.close()

print()
with open("geek.txt") as file:   
    data = file.read(5) 
    file.seek(5)
    print(data)
    data = file.read()  # # the file handle locates at 5
    print(data)
    print()
    file.seek(0) # moving the file handle to the beginning 
    data = file.read() 
    print(data)

    
#'''