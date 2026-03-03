class Solution:
    def solution(self):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        
        d = []
        
        for i in range(n - 1):
            d.append(a[i + 1] - a[i])
        
        
        d.sort()
        
        
        print(sum(d[:n-k]))


        

if __name__ == '__main__':
    sol = Solution()
    sol.solution()