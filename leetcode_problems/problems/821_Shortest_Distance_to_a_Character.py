'''
Created on Aug. 26, 2022

@author: AsifMahmud
'''
def shortestToChar(self, s: str, c: str) -> List[int]:
    answer = []
    len_s = len(s)
    for i in range(len_s):
        if s[i] == c:
            answer.append(0)
        else:
            left = s[0:i+1][::-1].find(c)
            right = s[i:len_s].find(c)
            if left == -1:
                left = 100000
            elif right == -1:
                right = 100000
            temp = left if left < right else right
            answer.append(temp)
    return answer