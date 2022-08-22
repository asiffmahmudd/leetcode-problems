'''
Created on Aug. 21, 2022

@author: AsifMahmud
'''
def largestTriangleArea(self, points: List[List[int]]) -> float:
    maxArea = 0
    for p1, p2, p3 in combinations(points, 3):
        area = (1/2) * abs(p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))
        if area > maxArea:
            maxArea = area
    return maxArea