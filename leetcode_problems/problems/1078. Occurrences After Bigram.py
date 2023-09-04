def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        i = 1
        arr = text.split(" ")
        result = []
        while i < len(arr):
            i += 1
            if arr[i-2] == first and arr[i-1] == second:
                if i < len(arr):
                    result.append(arr[i])
            
        return result