class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        pat = defaultdict(list)
        final = []
        for path in paths:
            path = path.split(" ")
            
            for i in range(1, len(path)):
                name, content = path[i].split('(')
                content = content[:-1]
                pat[content].append(path[0] + "/" + name)


        for m in pat.values():
            if len(m) > 1:
                final.append(m)
        return final