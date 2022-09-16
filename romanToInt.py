# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'IV':4,'IX':9, 'V':5,'X':10,'XL':40,'XC':90,'L':50,
                 'C':100,'CD':400,'CM':900, 'D':500,'M':1000}
        
        for i in s:
            if i == 1:
                out = roman[i]
            out = out+roman[i]
        jint = out
        return jint
    
a = romanToInt('III')
