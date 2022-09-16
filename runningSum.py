# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 18:57:38 2022

@author: Nick
"""
class Solution(object):
    def runningSum(self, nums):
        self.nums = nums
        runSum = []
        allSum=0
        for num in nums:
            allSum = allSum + num
            runSum.append(allSum)
        return(runSum)
    
ob1 = Solution()
print(ob1.runningSum([1,1,3,4]))