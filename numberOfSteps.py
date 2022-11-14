# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:13:47 2022

@author: Nick
Leetcode problem 1342 - submitted 11/7/2022- Success
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        self.num = num
        
        steps = 0
        while num !=  0:
            if num%2 == 0:
                num = num/2
                steps = steps+1
            else:
                num = num -1
                steps = steps+1
        return steps
        
obj = Solution()

num = 14
print(obj.numberOfSteps(num))

num = 8
print(obj.numberOfSteps(num))

num = 123
print(obj.numberOfSteps(num))
