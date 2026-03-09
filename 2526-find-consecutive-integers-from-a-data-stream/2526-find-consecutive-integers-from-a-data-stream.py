from collections import deque

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.q = deque()     
        self.count = 0        

    def consec(self, num: int) -> bool:
        self.q.append(num)
        if num == self.value: self.count += 1

        if len(self.q) > self.k:
            r = self.q.popleft()
            if r == self.value: self.count -= 1

        return len(self.q) == self.k and self.count == self.k