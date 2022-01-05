'''
Created on Jan 5, 2022

@author: AsifMahmud
'''

def convertToTitle(self, columnNumber: int) -> str:
    title = ""
    curr_char = ""
    while columnNumber > 26:
        columnNumber, remainder = divmod(columnNumber, 26)
        if remainder == 0:
            curr_char = "Z"
            columnNumber -= 1
        else:
            curr_char = chr(64+remainder)
        
        title += curr_char 
    
    columnNumber, remainder = divmod(columnNumber, 26)
    
    
    if remainder == 0:
        curr_char = "Z"
    else:
        curr_char = chr(64+remainder)
    title += curr_char
    return title[::-1]