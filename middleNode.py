# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:49:09 2022

@author: Nick
"""

class Solution:
    def middleNode(self, head):
        self.head = head
        
        mid = len(head)//2
        output = head[mid:]
        return output
        
obj = Solution()

head = [1,2,3,4,5]
print(obj.middleNode(head))

head = [1,2,3,4,5,6]
print(obj.middleNode(head))