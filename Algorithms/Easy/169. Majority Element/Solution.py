"""
Approach: Dictionary (map)

47 / 47 test cases passed.
Status: Accepted

Runtime: 168 ms
Memory Usage: 15.4 MB

Problem link: https://leetcode.com/problems/majority-element/
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums) / 2
        
        for x in nums:
            try:
                count[x] = count[x] + 1
            except:
                count[x] = 1
                
        for key in count:
            if count[key] > n:
                return key
        
        return -1
        