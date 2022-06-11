'''
Created on Jun 9, 2022

@author: AsifMahmud
'''
def findRelativeRanks(self, score: List[int]) -> List[str]:
    score_sorted = sorted(score, reverse=True)
    score_len = len(score)
    score_dict = {}
    
    for i in range(score_len):
        if(i == 0):
            score_dict[score_sorted[i]] = "Gold Medal"
        elif(i == 1):
            score_dict[score_sorted[i]] = "Silver Medal"
        elif(i == 2):
            score_dict[score_sorted[i]] = "Bronze Medal"
        else:
            score_dict[score_sorted[i]] = str(i+1)
            
    for i in range(score_len):
        score[i] = score_dict[score[i]]
        
    return score