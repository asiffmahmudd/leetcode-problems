'''
Created on May 8, 2022

@author: AsifMahmud
'''
def __init__(self):
        self.counter = []

def ping(self, t: int) -> int:
    start = t - 3000
    self.counter.append(t)
    count = 0
    len_counter = len(self.counter)
    
    for i in range(len_counter-1, -1, -1):
        if self.counter[i] >= start and self.counter[i] <= t:
            count += 1
        elif self.counter[i] < start:
            break
    return count