class FrequencyTracker(object):

    def __init__(self):
       self.freq = {}
       self.freq_cnt = {}
        
    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        old = self.freq.get(number, 0)
        if (old > 0):
            self.freq_cnt[old] -= 1

        neww = old + 1
        self.freq[number] = neww
        self.freq_cnt[neww] = self.freq_cnt.get(neww, 0) + 1

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        old = self.freq.get(number, 0)
        if (old <= 0): return

        self.freq_cnt[old] -= 1

        if (old == 1):
            del self.freq[number]
            return

        self.freq[number] = old - 1
        neww = old - 1

        self.freq_cnt[neww] = self.freq_cnt.get(neww, 0) + 1

    def hasFrequency(self, frequency):
        return self.freq_cnt.get(frequency, 0) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)