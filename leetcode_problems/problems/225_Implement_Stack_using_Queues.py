'''
Created on Jan 18, 2022

@author: AsifMahmud
'''
class MyStack:

    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) > 0:
            temp = self.arr[-1] 
            del self.arr[-1]
            return temp

    def top(self) -> int:
        if len(self.arr) > 0:
            return self.arr[len(self.arr)-1]

    def empty(self) -> bool:
        if len(self.arr) > 0:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()