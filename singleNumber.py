# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:17:46 2022

@author: Nick
"""
class Solution(object):
    def singleNumber(self, nums):
        self.nums = nums
        
        for num in nums:
            if nums.count(num) == 1:
                return(num)

obj = Solution()

nums = [1]

print(obj.singleNumber(nums))