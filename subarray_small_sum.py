from collections import defaultdict

class Solution:
    def solution(self):
        
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        l = 0
        count = 0
        seen = defaultdict(int)
        
        
        for r in range(n):
            
            seen[a[r]] += 1
            
            
            while (len(seen) > s):
                
                seen[a[l]] -= 1
                if (seen[a[l]] == 0): del seen[a[l]]
                l += 1
            
            count += r - l + 1
        print(count)
        
if __name__ == '__main__':
    sol = Solution()
    sol.solution()
