"""
Approach: bitwise operation

46 / 46 test cases passed.
Status: Accepted

Runtime: 492 ms
Memory Usage: 15.3 MB

Problem link: https://leetcode.com/problems/total-hamming-distance
"""

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        tot = 0
        for x in range(0, 32):
            set_bit = 0
            for val in nums:
                set_bit += (val >> x) & 1
            tot += set_bit * (len(nums) - set_bit)
        return tot