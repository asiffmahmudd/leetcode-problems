'''
Created on Jan 12, 2022

@author: AsifMahmud
'''

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None or head.next == None:
        return head
    curr = head.next
    prev = head
    
    while(curr.next != None):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    curr.next = prev
    head.next = None
    return curr