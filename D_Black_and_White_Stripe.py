class Solution:
    def solution(self):
        t = int(input())
        for _ in range(t):
            n, k = map(int, input().split())
            s = input()
            
            l = 0
            final = float('inf')
            count = 0
            
            for r in range(n):


                if r - l + 1 > k:
                    if (s[l] == "W"): count -= 1
                    l += 1                
                if s[r] == "W": count += 1
                if r - l + 1 == k: final = min(final, count)
                
                    
                r += 1
            print(final)
           

if __name__ == "__main__":
    Solution().solution()
