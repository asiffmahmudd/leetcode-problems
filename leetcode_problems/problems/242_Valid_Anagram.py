'''
Created on Feb 20, 2022

@author: AsifMahmud
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        
        s_dict = {}
        t_dict = {}
        for i,j in zip(s, t):
            if i in s_dict.keys():
                s_dict.update({i:s_dict[i]+1})
            else:
                s_dict[i] = 1
            if j in t_dict.keys():
                t_dict.update({j:t_dict[j]+1})
            else:
                t_dict[j] = 1    
        for key in s_dict:
            if key not in t_dict.keys():
                return False
            elif s_dict[key] != t_dict[key]:
                return False
        return True