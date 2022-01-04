'''
Created on Jan 4, 2022

@author: AsifMahmud
'''

def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        result = []
        while i < j:
            sum = numbers[i]+numbers[j]
            if(sum == target):
                result.append(i+1)
                result.append(j+1)
                break
            elif sum > target:
                j -= 1
            else:
                i += 1
        return result