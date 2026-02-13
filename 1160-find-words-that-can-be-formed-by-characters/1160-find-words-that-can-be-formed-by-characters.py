class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        final_sum = 0
        char_count = defaultdict(int)

        for char in chars:
            char_count[char] += 1
           
        for word in words:
            word_count = defaultdict(int)
            for char in word:
                word_count[char] += 1

            flag = True
            for i, j in word_count.items():
                if (char_count[i] < j):
                    flag = False
                    break
            if (flag): final_sum += len(word)

        return final_sum;

       
        