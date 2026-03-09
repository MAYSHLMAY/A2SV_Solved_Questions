class Solution:
    def simplifyPath(self, path: str) -> str:
        

        path = path.split("/")
        stack = []
        # final = ""

        for dirs in path:

            if dirs == "." or dirs == "":
                continue
            if dirs == "..":
                if (stack): stack.pop()
            else:
                stack.append(dirs)
        
        if (not stack): return "/";
        return "/" + "/".join(stack)