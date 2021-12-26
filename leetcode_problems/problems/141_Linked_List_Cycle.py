'''
Created on Dec 25, 2021

@author: AsifMahmud
'''

def hasCycle(self, head: Optional[ListNode]) -> bool:
    temp = head
    f = 0
    while temp != None:
        if temp != None:
            if temp.val == None:
                f = 1
                break
            temp.val = None
        temp = temp.next
    if f == 0:
        return False
    else:
        return True