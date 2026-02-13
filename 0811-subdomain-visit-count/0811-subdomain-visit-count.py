class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        counts = defaultdict(int)

        for cpdomain in cpdomains:
            count, subdomain = cpdomain.split(" ")
            count = int(count)

            counts[subdomain] += count
            for i, char in enumerate(subdomain):
                if char == ".":
                     counts[subdomain[i+1:]] += count
        
        return [f"{v} {k}" for k, v in counts.items()]