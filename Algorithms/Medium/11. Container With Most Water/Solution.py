"""
60 / 60 test cases passed.
Status: Accepted

Runtime: 752 ms
Memory Usage: 27.5 MB

Problem link: https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0; j = len(height)-1; ans = -inf
        while i < j:
            ans = max(ans, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]: i += 1
            else: j -= 1
        return ans
        