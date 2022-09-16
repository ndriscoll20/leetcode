# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:33:58 2022

@author: Nick
"""
class Solution(object):
    def twoSum(self, nums: [int], target: int) -> [int]:
        self.nums = nums
        self.target = target
        for i, num in enumerate(nums):
            try:
                nums.index(target-num)
                if nums.index(target-num)== i:
                    continue
                else:
                    j = nums.index(target-num)
                    return([i,j])
            except:
                continue
            
            '''
            for j, num2 in enumerate(nums):
                if i==j:
                    continue
                elif num+num2 == target:
                    return([i,j])
              '''  
obj = Solution()

nums = [3,2,3]
target = 6

print(obj.twoSum(nums, target))