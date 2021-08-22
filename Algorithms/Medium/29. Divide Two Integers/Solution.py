"""
992 / 992 test cases passed.
Status: Accepted

Runtime: 32 ms
Memory Usage: 14.3 MB

Problem link: https://leetcode.com/problems/divide-two-integers/
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        mx = 2 ** 31
        x = int(dividend / divisor)
        if x < -mx: return -mx
        elif x > mx - 1: return mx - 1
        return x