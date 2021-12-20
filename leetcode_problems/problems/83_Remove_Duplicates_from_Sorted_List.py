'''
Created on Dec 17, 2021

@author: AsifMahmud
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        temp = head
        while(temp.next != None ):
            if(temp.next != None):
                if(temp.val == temp.next.val):
                    temp2 = temp.next
                    temp.next = temp.next.next
                    del(temp2)
                else:
                    temp = temp.next
        return head