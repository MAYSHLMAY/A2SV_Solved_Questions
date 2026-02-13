class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = {}
        final_sum = 0

        for word in words:
            for char in word:
                counts[char] = counts.get(char, 0) + 1
            
            for char2 in chars:
                if char2 in counts:
                    counts[char2] -= 1
            is_cancelled = all(val <= 0 for val in counts.values())
            counts = {}
            if is_cancelled:
                final_sum += len(word)
        return final_sum;

       
        