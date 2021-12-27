'''
Created on Dec 27, 2021

@author: AsifMahmud
'''

def maxProfit(self, prices: List[int]) -> int:
    min_stock = prices[0]
    max_stock = prices[0]
    i = 0
    j = 0
    max_profit = 0
    for index in range(1, len(prices)):
        if(min_stock > prices[index]):
            min_stock = prices[index]
            max_stock = prices[index]
            i = index
            j = index
        if(max_stock < prices[index]):
            max_stock = prices[index]
            j = index
            if(max_stock - min_stock > max_profit):
                max_profit = max_stock - min_stock
    
    return max_profit
        