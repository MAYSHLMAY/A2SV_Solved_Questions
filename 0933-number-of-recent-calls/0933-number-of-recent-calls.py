class RecentCounter:

    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        # Remove all requests NOT in the range [t-3000, t]
        while self.q and not (t - 3000 <= self.q[0] <= t):
            self.q.pop(0)
        
        self.q.append(t)
        return len(self.q)