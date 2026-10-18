class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        self.mini = []

        # [1,0,-1,2,4,3,-2]
        # [1,0,-1,-2]
        # [2,4,3]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        elif self.mins[-1] < val:
            self.mini.append(val)
        else:
            self.mins.append(val)
        
    def pop(self) -> None:
        k = self.stack.pop(-1)
        if k == self.mins[-1]:
            self.mins.pop(-1)
        else:
            self.mini.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]

        
