class RecentCounter:

    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        while self.q and not (t - 3000 <= self.q[0]):
            self.q.pop(0)
        
        self.q.append(t)
        return len(self.q)