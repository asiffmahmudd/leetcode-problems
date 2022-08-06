'''
Created on Aug. 5, 2022

@author: AsifMahmud
'''
def countPrimeSetBits(self, left: int, right: int) -> int:
    def isPrime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        elif n > 2 and n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n%i == 0:
                return False
        return True
    
    count = 0
    for i in range(left, right+1):
        if(isPrime(format(i, "b").count('1'))):
           count += 1
    return count