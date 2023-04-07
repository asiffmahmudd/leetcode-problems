def canThreePartsEqualSum(self, arr: List[int]) -> bool:
    total = sum(arr)
    if total % 3 != 0:
        return False
    eachPart = total // 3
    tmp = count = 0

    for num in arr:
        if count == 2:
            return True
        tmp += num
        if tmp == eachPart:
            count += 1
            tmp = 0
    return False