class Solution:
    def solution(self):
        t = int(input())
        
        
        for _ in range(t):
            n, k = map(int, input().split())
            
            c = []
            
            for _ in range(n):
                
                l, r, v = map(int, input().split())
                c.append((l, r, v))
                
            c.sort()
            
            a = k
            
            for l, r, v in c:
                if l <= a <= r: a = max(a, v)
            
            print(a)

if __name__ == '__main__':
    sol = Solution()
    sol.solution()