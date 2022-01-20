"""
211 / 211 test cases passed.
Status: Accepted

Runtime: 1200 ms
Memory Usage: 25.2 MB

Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo, ans = prices[0], 0
        for x in prices:
            if x - lo > ans: ans = x - lo
            if x < lo: lo = x
        return ans
        