# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:48:24 2016

@author: Aditya
"""

class Solution:
    def isAnagram(self,s,t):
        countArray = [0]*256
        
        for i in s:
            countArray[ord(i)] +=1
    
        for j in t:
            countArray[ord(j)] -=1
            if countArray[ord(j)] < 0:
                return False
        return sum(countArray) == 0
        