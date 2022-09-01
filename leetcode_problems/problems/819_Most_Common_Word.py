'''
Created on Aug. 22, 2022

@author: AsifMahmud
'''
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    wordFrequency = {}
    paragraph = re.findall(r'\w+', paragraph)
    for word in paragraph:
        word = word.lower()
        if word not in banned:
            if word not in wordFrequency:
                wordFrequency[word] = 1
            else:
                wordFrequency[word] += 1
    return max(wordFrequency, key = wordFrequency.get)