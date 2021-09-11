"""
Approach: Dictionary (map)

82 / 82 test cases passed.
Status: Accepted

Runtime: 149 ms
Memory Usage: 15.5 MB

Problem link: https://leetcode.com/problems/majority-element-ii/
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums) // 3
        ans = []
        
        for x in nums:
            try:
                count[x] = count[x] + 1
            except:
                count[x] = 1
                
        for key in count:
            if count[key] > n:
                ans.append(key)
        
        return ans
        