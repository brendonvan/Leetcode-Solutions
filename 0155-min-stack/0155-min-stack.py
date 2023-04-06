class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val)) 
            return
        current_min = self.stack[-1][1]
        
        self.stack.append((val, min(val, current_min))) #O(1)

    def pop(self) -> None:
        self.stack.pop() # O(1)

    def top(self) -> int:
        return self.stack[-1][0] # O(1)

    def getMin(self) -> int: 
        # for loop through stack and find lowest value O(n)
        
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()