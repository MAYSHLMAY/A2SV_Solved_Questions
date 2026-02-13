class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final = defaultdict(list)
        for stri in strs:
            key = "".join(sorted(stri))
            final[key].append(stri)
        return list(final.values())