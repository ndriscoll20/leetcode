# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:20:43 2022

@author: Nick
"""
class Solution(object):
    def rotate(self, nums, k):
        self.nums = nums
        self.k = k
                
        #nums = nums[len(nums)-k:len(nums)] + nums[0:len(nums)-k]
        for i in range(k):
            nums.insert(0, nums.pop())
        
        return(nums)
    
obj = Solution()

nums = [1,2,3,4,5,6,7]
k = 3
print(obj.rotate(nums,k))