# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 12:14:56 2022

@author: Nick
"""
class Solution(object):
    def isSubsequence(self, s, t):
        self.s = s
        self.t = t
        
        if len(s) > len(t):
            return(False)
        count = 0
        for i in range(len(t)):
            if count == len(s):
                break
            elif s[count] == t[i]:
                count=count+1
        return(len(s)==count)
                
            
        

obj = Solution()

s = 'ahbd'
t = 'ahbgdc'
print(obj.isSubsequence(s,t))