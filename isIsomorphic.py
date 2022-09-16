# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 08:53:55 2022

@author: Nick
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        self.s = s
        self.t = t
        S={}
        for idx in range(len(s)): 
            if s[idx] not in S.keys():
                if t[idx] not in S.values():
                    S[s[idx]] = t[idx]
                else:
                    return(False)
            elif S[s[idx]] == t[idx]:
                continue
            else:
                return(False)
        return(True)
    
obj = Solution()
string1 = 'badc'
string2 = 'baba'
print(obj.isIsomorphic(string1, string2))