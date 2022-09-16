# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 18:58:37 2022

@author: Nick
"""

class Solution:
    def __init__(self):
        pass
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        tmp = str(x)
        rev = tmp[::-1]
        output = tmp == rev
        return(output)

solution=Solution() 
print(solution.isPalindrome(12321))