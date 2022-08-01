'''
Created on Aug. 1, 2022

@author: AsifMahmud
'''
def minCostClimbingStairs(self, cost: List[int]) -> int:
    n = len(cost)
    for i in range(2, n):
        cost[i] += min(cost[i-1], cost[i-2])
    return min(cost[n-1], cost[n-2])