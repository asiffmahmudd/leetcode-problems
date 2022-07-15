'''
Created on Jul. 12, 2022

@author: AsifMahmud
'''
def calPoints(self, ops: List[str]) -> int:
    record = []
    for op in ops:
        if op == "C":
            record = record[:-1]
        elif op == "D":
            print(op, record)
            record.append(record[-1]*2)
        elif op == "+":
            record.append(record[-1]+record[-2])
        else:
            record.append(int(op))
    return sum(record)