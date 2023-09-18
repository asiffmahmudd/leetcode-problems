def duplicateZeros(self, arr: List[int]) -> None:
    i = 0
    arr_len = len(arr)
    def shiftElements(index):
        i = arr_len-1
        while i > index:
            arr[i] = arr[i-1]
            i -= 1
    while(i < arr_len):
        if(arr[i] == 0 and i+1 < arr_len):
            shiftElements(i)
            i += 1
        i += 1