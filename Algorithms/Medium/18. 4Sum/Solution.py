"""
Approach: map


286 / 286 test cases passed.
Status: Accepted

Runtime: 1644 ms
Memory Usage: 14.4 MB

Problem link: https://leetcode.com/problems/4sum/
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        mp = {}
        for i in range(3, length):
            mp[target-nums[i]] = i
        ans = set()
        for i in range(0, length-3):
            for j in range(i+1, length-2):
                for k in range(j+1, length-1):
                    val = mp.get(nums[i] + nums[j] + nums[k], -1)
                    if val > k:
                        ans.add((nums[i], nums[j], nums[k], nums[val]))
        return list(ans)