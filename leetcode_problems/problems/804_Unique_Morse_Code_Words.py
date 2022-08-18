'''
Created on Aug. 18, 2022

@author: AsifMahmud
'''
def uniqueMorseRepresentations(self, words: List[str]) -> int:
    codes = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
    
    morseWords = []
    for word in words:
        code = ""
        for ch in word:
            code += codes[ch]
        morseWords.append(code)
    return len(set(morseWords))