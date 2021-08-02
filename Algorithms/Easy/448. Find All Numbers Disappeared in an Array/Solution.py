"""
Approach: map


33 / 33 test cases passed.
Status: Accepted

Runtime: 340 ms
Memory Usage: 21.8 MB

Problem link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mx = len(nums) + 1
        mp = [0 for i in range(mx)]
        for x in nums: mp[x] = 1
        
        result = []
        for i in range(1, mx):
            if not mp[i]:
                result.append(i)
        return result
        