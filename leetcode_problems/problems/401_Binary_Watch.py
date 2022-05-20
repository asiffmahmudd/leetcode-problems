'''
Created on May 20, 2022

@author: AsifMahmud
'''
def readBinaryWatch(self, turnedOn: int) -> List[str]:
    result = []
    for hour in range(12):
        for min in range(60):
            s = str(bin(hour)) + str(bin(min))
            if s.count('1') == turnedOn:
                s = str(hour) + ':' + "{:02d}".format(min)
                result.append(s)
    return result