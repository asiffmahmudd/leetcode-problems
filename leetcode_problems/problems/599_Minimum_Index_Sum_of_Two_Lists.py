'''
Created on Jun. 24, 2022

@author: AsifMahmud
'''
def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    result = []
    minIndex = 99999
    for restaurant in list1:
        if restaurant in list2:
            idx1 = list1.index(restaurant)
            idx2 = list2.index(restaurant)
            if(idx1 + idx2 < minIndex):
                minIndex = idx1 + idx2
                result = [restaurant]
            elif idx1 + idx2 == minIndex:
                result.append(restaurant)
    return result