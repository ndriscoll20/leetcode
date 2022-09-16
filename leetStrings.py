# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 17:50:53 2022

@author: Nick
"""
#import collections
class Solution:
    def reverseString(self, s: [str]) -> None:
        s[:] = s[::-1]
    
    def firstUniqueChar(self,s: str) -> int:
        t = list(s)
        for i, ch in enumerate(t): 
            if t.count(ch) == 1:
                return(i)
        return(-1)
        #Using a hash map: 
        # count = collections.Counter(s)
        
        # for idx, ch in enumerate(s):
        #     if count[ch] == 1:
        #         return idx
        # return -1
            
    def myAtoi(self, s:str) -> int:
        s=s.strip()
        neg = False
        idx =0
        if len(s)==0:
            return(0)
        if s[0] == '-':
            neg = True
            s=s.replace('-','')
            if len(s) == 0:
                return(0)
        elif s[0] =='+': 
            s = s.replace('+','')
            neg = False
            if len(s)==0:
                return(0)
        for ch in s:
            #ch.isdigit()
            try:
                isinstance(int(ch),int)
                idx+=1
            except:
                break
        if idx == 0:
            try:
                isinstance(s[0],str)
                return(0)
            except:
                print()
        if neg:
            out = -1*int(s[0:idx])
        else:
            out = int(s[0:idx])
        if out > 2**31 - 1:
            out = 2**31 - 1
        elif out < -2**31:
            out = -2**31
        
        return(out, type(out))
    
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return(haystack.index(needle))
        else: 
            return(-1)
    
obj = Solution()
# s = ["h","e","l","l","o"]
# obj.reverseString(s)
# print(s)

# s = 'leetcode'
# print(obj.firstUniqueChar(s))

# s = " -42"
# print(obj.myAtoi(s))

haystack = 'leetcode'
needle = 'leeto'
print(obj.strStr(haystack, needle))