class Solution:
    def solution(self):
        
        res = []
        for i in range(5):
            row = list(map(int, input().split()))
            if (1 in row):
                res.append(i)
                res.append(row.index(1))
                break
            
        print(abs(3 - (res[0] + 1)) + abs(3 - (res[1] + 1)))

if __name__ == '__main__':
    sol = Solution()
    sol.solution()