# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:04:24 2022

@author: Nick
"""

class Solution:
    def maximizeWealth(self, accounts) -> int:
        totalWealth = []
        for i in range(len(accounts)):
            totalWealth.append(sum(accounts[i][:]))
        return(max(totalWealth))
        
obj = Solution()

#accounts = [[1,2,3],[3,2,1]]
#accounts = [[1,5],[7,3],[3,5]]
accounts = [[2,8,7],[7,1,3],[1,9,5]]

print(obj.maximizeWealth(accounts))        