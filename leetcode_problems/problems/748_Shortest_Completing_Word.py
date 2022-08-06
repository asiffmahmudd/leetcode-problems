'''
Created on Aug. 5, 2022

@author: AsifMahmud
'''
def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
    licensePlate = licensePlate.lower()
    licensePlateFrequency = dict(Counter(licensePlate))
    foundWords = []
    result = "asdfghjklpoiuytrewqzxcvbnm"
    for word in words:
        wordFrequency = dict(Counter(word))
        found = True
        for letter in licensePlateFrequency.keys():
            if letter.isalpha():
                if letter in wordFrequency:
                    if licensePlateFrequency[letter] > wordFrequency[letter]:
                        found = False
                        break
                else:
                    found = False
                    break
        if found and len(result) > len(word):
            result = word
    return result