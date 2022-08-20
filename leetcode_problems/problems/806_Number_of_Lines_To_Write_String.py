'''
Created on Aug. 20, 2022

@author: AsifMahmud
'''
def numberOfLines(self, widths: List[int], s: str) -> List[int]:
    lineCount = 1
    currWidth = 0
    
    for ch in s:
        if currWidth + widths[ord(ch) - 97] > 100:
            lineCount += 1
            currWidth = 0
        currWidth += widths[ord(ch) - 97]
    return [lineCount, currWidth]