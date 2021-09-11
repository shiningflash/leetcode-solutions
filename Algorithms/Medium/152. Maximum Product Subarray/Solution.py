"""
187 / 187 test cases passed.
Status: Accepted

Runtime: 85 ms
Memory Usage: 14.4 MB

Problem link: https://leetcode.com/problems/maximum-product-subarray/
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        positive, negative, result = nums[0], nums[0], nums[0]
        for x in nums[1:]:
            positive, negative = max(x, positive*x, negative*x), min(x, positive*x, negative*x)
            result = max(positive, result)
        return result