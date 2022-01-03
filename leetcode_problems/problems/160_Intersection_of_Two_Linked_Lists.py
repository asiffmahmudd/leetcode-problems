'''
Created on Jan 3, 2022

@author: AsifMahmud
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        tempA = headA
        tempB = headB
        lenA = 0
        lenB = 0
        result = None
        
        while tempA:
            lenA += 1
            tempA = tempA.next
        while tempB:
            lenB += 1
            tempB = tempB.next
        diff = abs(lenA-lenB)
        
        if(lenA > lenB):
            for i in range(diff):
                headA = headA.next
        else:
            for i in range(diff):
                headB = headB.next
                
        tempA = headA
        tempB = headB
        
        while tempA and tempB and tempA != tempB:
            tempA = tempA.next
            tempB = tempB.next
        return tempA