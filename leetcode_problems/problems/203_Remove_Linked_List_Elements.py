'''
Created on Jan 10, 2022

@author: AsifMahmud
'''
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    curr = head
    if head != None:
        curr = head.next
    prev = head
    while curr != None:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    if head != None and head.val == val:
        head = head.next
    return head