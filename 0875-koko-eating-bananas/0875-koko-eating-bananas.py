class Solution:
    def minEatingSpeed(self, p, h):
        l = 1
        r = max(p)

        while l < r:
            m = (l + r) // 2
            
            t = 0
            for x in p:

                t += x // m
                if x % m != 0:
                    t += 1

            if t <= h:
                r = m
            else:
                l = m + 1

        return l