class Solution:
    def solution(self):
        for _ in range(int(input())):
            
            n = int(input())
            a = list(map(int, input().split()))
            b = list(map(int, input().split()))
            
            ops = []
            
            flag = False
            while not flag:
                flag = True
                for i in range(n):
                    if a[i] > b[i]:
                        a[i], b[i] = b[i], a[i]
                        ops.append((3, i + 1))
                        flag = False
                    if i < n - 1:
                        if a[i] > a[i + 1]:
                            a[i], a[i + 1] = a[i + 1], a[i]
                            ops.append((1, i + 1))
                            flag = False
                        if b[i] > b[i + 1]:
                            b[i], b[i + 1] = b[i + 1], b[i]
                            ops.append((2, i + 1))
                            flag = False
            print(len(ops))
            for type, idx in ops:
                print(type, idx)

if __name__ == '__main__':
    sol = Solution()
    sol.solution()