class Solution:
    def solution(self):
        
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        l = 0
        count = 0
        _sum = 0
        for r in range(n):
            _sum += a[r]
            
            while (_sum > s - 1):
                _sum -= a[l]
                l += 1
            
            count += r - l + 1
        print(((n * (n + 1)) // 2) - count)
        
if __name__ == '__main__':
    sol = Solution()
    sol.solution()
