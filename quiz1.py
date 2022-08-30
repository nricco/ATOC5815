# -*- coding: utf-8 -*-
"""
Quiz #1 8/30/2022

@author: nricc
Write a python code with the following functions: input 3 numbers, 
then decide whether they are an even or odd number and print out results
DONT USE any existing Python math functions. 
"""
def oddOrEven(a_1, a_2, a_3):
    '''
    Parameters
    ----------
    a_1 : Int
    a_2 : Int
    a_3 : Int

    Returns
    -------
    None.

    '''
    x = [a_1, a_2, a_3]
    
    for i in x: 
        # Use modulus operator to test even or odd input
        if( i % 2 == 0 ):
            print(i, "is an even number.")
        else:
            print(i, "is an odd number")

# Test 1
oddOrEven(2,7,11)
# Test 2
oddOrEven(120,1213,378)
        

