class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        dictt = {r: i for i, r in enumerate(list1)}
        min_sum = float("inf")
        res = []
        current_sum = 0
        for i, r in enumerate(list2):
            if r in dictt:
                current_sum = i + dictt[r]
            
                if current_sum < min_sum:
                    min_sum = current_sum
                    res = [r]
                elif current_sum == min_sum:
                    res.append(r)
            else:
                continue
        return res
        