class Stack:
    def __init__(self,stack):
        self.stack = []
        self.mini = float("inf") # record minimum number using greedy
        #self.minus = 0



    def push(self,n):
        if len(self.stack) == 0:
            self.mini = n
            self.stack.append(n)

        if n >= self.mini:
            self.stack.append(n)
        else:
            # if self.mini < 0:
            #     self.minus = 1

            self.stack.append(n-self.mini)

            self.mini = n

    def pop(self):
        val = self.stack[-1]
        if val >= self.mini:
            return self.stack.pop()
        else: # val < self.mini need to recover
            yz = self.stack.pop()
            self.mini -= yz

            return yz+self.mini



    def getMin(self):
        return self.mini
