"""
Approach: Maximum Subarray Sum

203 / 203 test cases passed.
Status: Accepted

Runtime: 52 ms
Memory Usage: 14.9 MB

Problem link: https://leetcode.com/problems/maximum-subarray/
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)

        cur_max, global_max = 0, 0

        for x in nums:
            cur_max += x
            if cur_max < 0:
                cur_max = 0
            elif cur_max > global_max:
                global_max = cur_max
                
        return global_max