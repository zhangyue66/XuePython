class RLEIterator:

    def __init__(self, A):
        self.A = A
        self.i = 0


    def next(self, n: int) -> int:
        while self.i < len(self.A) and self.A[self.i] < n:
            n -= self.A[self.i]
            self.i += 2
        if self.i >= len(self.A):
            return -1
        self.A[self.i] -= n
        return self.A[self.i+1]
