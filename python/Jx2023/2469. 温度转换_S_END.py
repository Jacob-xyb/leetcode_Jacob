"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/29 17:16"
"""
from typing import *


# https://leetcode.cn/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32
        return [kelvin, fahrenheit]


if __name__ == '__main__':
    celsius = 36.50
    print(Solution().convertTemperature(celsius))

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/29 17:18"
"""
