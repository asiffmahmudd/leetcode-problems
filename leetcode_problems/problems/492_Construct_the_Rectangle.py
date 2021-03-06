'''
Created on Jun 2, 2022

@author: AsifMahmud
'''
# efficient one
# def constructRectangle(self, area: int) -> List[int]:
#     peak = int(area ** 0.5)
#
#     for i in range(peak, 0, -1):
#         if(area % i == 0):
#             return [int(max(i, area / i)), int(min(i, area / i))]


def constructRectangle(self, area: int) -> List[int]:
    l = math.ceil(area/2)
    multiples = []
    while l >= 1:
        if area % l == 0:
            if area // l > l:
                multiples.append([area//l, l])
            else:
                multiples.append([l, area//l])
        l -= 1
    min_diff = 9223372036854775807
    index = 0
    for i in range(len(multiples)):
        if(multiples[i][0] - multiples[i][1] < min_diff):
            min_diff = multiples[i][0] - multiples[i][1]
            index = i
    
    return multiples[index]