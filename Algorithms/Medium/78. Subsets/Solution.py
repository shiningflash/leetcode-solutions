"""
Approach: bitwise approach

10 / 10 test cases passed.
Status: Accepted

Runtime: 28 ms
Memory Usage: 14.3 MB

Problem link: https://leetcode.com/problems/subsets/
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        for i in range(1 << length):
            subset = []
            for j in range(length):
                if i & (1 << j):
                    subset.append(nums[j])
            ans.append(subset)
        return ans
        