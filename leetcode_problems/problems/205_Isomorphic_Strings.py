'''
Created on Jan 11, 2022

@author: AsifMahmud
'''

def isIsomorphic(self, s: str, t: str) -> bool:
    s_count = {}
    t_count = {}
    for s_char, t_char in zip(s,t):
        if s_char not in s_count:
            s_count.update({s_char:1})
        else:
            curr_value = s_count[s_char]
            s_count[s_char] = curr_value + 1
            
        if t_char not in t_count:
            t_count.update({t_char:1})
        else:
            curr_value = t_count[t_char]
            t_count[t_char] = curr_value + 1
     
    result_dictionary = {}
    
    s_keys = list(dict.keys(s_count))
    t_keys = list(dict.keys(t_count))
    s_values = list(dict.values(s_count))
    t_values = list(dict.values(t_count))
    
    for key, value in s_count.items():
        position = -1
        if value in t_values:
            position = t_values.index(value)
        if position == -1:
            result_dictionary.update({key:"0"})
        else:
            result_dictionary.update({key:t_keys[position]})
        t_values[position] = -1
        
    result = ""
    for char in s:
        result += result_dictionary[char]
    
    if result == t:
        return True
    else:
        return False