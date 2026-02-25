class Solution:
    def solution(self):
        t = int(input())
        
        
        arr = list(map(int, input().split())) 
        arr.sort()
        
        if (t % 2 == 1):
            print(arr[t//2])
        else:
            print(arr[t//2 - 1])
if __name__ == '__main__':
    sol = Solution()
    sol.solution()