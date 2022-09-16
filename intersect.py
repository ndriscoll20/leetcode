# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 16:45:58 2022

@author: Nick
"""
class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        # out = []
        # idx2 = []
        # for i, num in enumerate(nums1):
        #     for j, num2 in enumerate(nums2):
        #         if len(out) == len(nums1) or len(out) == len(nums2):
        #             break
        #         elif num == num2:
        #             if j in idx2:
        #                 continue
        #             out.append(num)
        #             idx2.append(j)
                    
        #             break
        # return(out)

        out = []
        d = {}
        for num in nums1:
            if num in d: 
                d[num] = nums1.count(num)
            else:
                d[num] = 1
        
        for num2 in nums2:
            if num2 in d and d[num2]>0:
                out.append(num2)
                d[num2]-=1
        
        return(out)
    
obj = Solution()
#nums1 = [1,2,2,1]
#nums2 = [2]
nums1 = [61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81]
nums2 = [5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]
print(obj.intersect(nums1,nums2))

