def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
    biNum = ''
    result = []
    for num in nums:
        biNum += str(num)
        if(int(biNum, 2) % 5 == 0):
            result.append(True)
        else:
            result.append(False)
    return result