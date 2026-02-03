class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [celsius * 9.0 / 5.0 + 32.0, celsius + 273.15]
