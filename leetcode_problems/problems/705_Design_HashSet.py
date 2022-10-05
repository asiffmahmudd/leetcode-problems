'''
Created on Oct. 4, 2022

@author: AsifMahmud
'''
def __init__(self):
    self.hashSet = [[] for _ in range(1000)]

def add(self, key: int) -> None:
    subkey = key%1000
    if not self.contains(key):
        self.hashSet[subkey].append(key)

def remove(self, key: int) -> None:
    subkey = key%1000
    if self.contains(key):
        self.hashSet[subkey].remove(key)

def contains(self, key: int) -> bool:
    subkey = key%1000
    return key in self.hashSet[subkey]