# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:36:08 2022

@author: Nick
"""
class Solution(object):
    def pivotIndex(self, nums):
        self.nums = nums
        runSum = 0
        leftSum,rightSum = [], []
        for num in nums:
            runSum = runSum + num
            leftSum.append(runSum)
        runSum = 0
        for num2 in reversed(nums):
            runSum = runSum + num2
            rightSum.append(runSum)
        for lidx in range(len(leftSum)):
            if lidx+1 > len(leftSum):
                return(-1)
            elif leftSum[lidx] == rightSum[lidx+1]:
                return(lidx)
            else:
                return(0)
        
obj = Solution()
nums = [1,7,3,6,5,6]
nums1 = [1,2,3]
nums2 = [2,1,-1]
print(obj.pivotIndex(nums))        