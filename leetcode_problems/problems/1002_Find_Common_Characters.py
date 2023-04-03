def commonChars(self, words: List[str]) -> List[str]:
    letters = words[0]
    result = []
    for letter in letters:
        flag = 0
        for i in range(1, len(words)):
            indx = words[i].find(letter)
            if indx >=0:
                words[i] = words[i].replace(letter, '*', 1)
            else:
                flag = 1
                break
        if flag == 0:
            result.append(letter)
    return result