class MinStack:

    def __init__(self):
        self.stk = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()
        if self.minStack:
            self.minStack.pop()    
        else:
            print("Stack is empty")
            return
        

    def top(self) -> int:
        if self.stk:
            return self.stk[-1]
        else:
            print("Stack is empty")
            return -1
        

    def getMin(self) -> int:
        return self.minStack[-1]

        
