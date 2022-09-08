#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:16:24 2020

@author: zhwa2432
"""


import fibonacci 
print(fibonacci.fib(7)) 

print(fibonacci.fib(20)) 

print(fibonacci.ifib(42))

'''
import sys
import textwrap
names = sorted(sys.modules.keys())
name_text = ', '.join(names)

print (textwrap.fill(name_text))


for name in sys.builtin_module_names:
    print(name)

print()
for d in sys.path:
    print(d)
'''