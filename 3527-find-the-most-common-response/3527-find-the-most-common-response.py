class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        if not responses:
            return ""
        seen_today = set()
        counts = defaultdict(int)

        for day_response in responses:
            seen_today = set()
            for response in day_response:
                if response not in seen_today:
                    counts[response] += 1
                    seen_today.add(response)
                    
        groups = []
        maxy = max(counts.values())
        for key, value in counts.items():
            if (value == maxy):
                groups.append(key)
        return min(groups)