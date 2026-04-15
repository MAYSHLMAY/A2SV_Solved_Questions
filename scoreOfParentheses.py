class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        depth = 0
        final = 0

        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
            else:
                depth -= 1
                if (s[i - 1] == "("): final += 2 ** (depth)
        return final
