# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 17:25:14 2022

@author: Nick
"""

s = 'MCMXCIV'
roman = {'I':1, 'V':5,'X':10,'L':50,
         'C':100,'D':500,'M':1000}
roman2 = {'IV':4,'IX':9,'XL':40,'XC':90,
         'CD':400,'CM':900}

count = 1

for i in s:
    if count == 1:
        out = roman[i]
        skip = False
    elif skip:
        skip = False
        count = count+1
        continue
    elif count < len(s):
        if (i + s[count]) in roman2.keys(): #count is already one ahead of index
            out = out + roman2[i+s[count]]
            skip = True
        else: 
            out = out+roman[i]
            skip = False
    elif count == len(s):
        out = out+roman[i]
        skip = False

    count = count+1

jint = out
