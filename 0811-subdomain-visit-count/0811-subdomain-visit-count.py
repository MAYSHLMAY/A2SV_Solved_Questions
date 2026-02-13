class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)
        final = []

        for cpdomain in cpdomains:
            count, subdomain = cpdomain.split(" ")

            subdomain = subdomain.split(".")
            print(subdomain)
            for i in range(len(subdomain)):
                temp = ".".join(subdomain[i:])
                counts[temp] += int(count)
        
        for keys, values in counts.items():
            final.append(str(values) + " " + keys)
        return final