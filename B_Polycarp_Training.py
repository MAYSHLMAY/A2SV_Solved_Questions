class Solution:
    def solution(self):
        t = int(input())
        
        
        arr = list(map(int, input().split())) 
        arr.sort()
        
        left = 1
        total = 0
        
        for m in range(t):
            if (arr[m] >= left):
                total += 1
                left += 1
        print(total)
if __name__ == '__main__':
    sol = Solution()
    sol.solution()