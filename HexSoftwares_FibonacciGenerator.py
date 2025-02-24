# -*- coding: utf-8 -*-
"""
@author: Serothwane Vincent
"""

# solving the fibonacci equation recursively

def fibonacci_recursive(n):
    # Base cases
    if n <= 0:
        return "Invalid input"
    
    elif n == 1:
        return 0
    
    elif n == 2:
        return 1
    
    # recursive case
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
    
    # tester
n=4
print([fibonacci_recursive(i) for i in range(1, n+1)])
