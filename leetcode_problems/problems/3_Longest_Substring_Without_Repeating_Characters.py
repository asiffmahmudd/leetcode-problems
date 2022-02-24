'''
Created on Feb 23, 2022

@author: AsifMahmud
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = []
        max_len = 0
        str_len = len(s)
        for char in s:
            while(char in substr):
                substr.pop(0)
            substr.append(char)
            max_len = max(max_len, len(substr))
        return max_len
            