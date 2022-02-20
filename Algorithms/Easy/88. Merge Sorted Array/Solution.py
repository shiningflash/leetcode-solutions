"""
Approach: iterative

59 / 59 test cases passed.
Status: Accepted

Runtime: 77 ms
Memory Usage: 13.8 MB

Problem link: https://leetcode.com/problems/merge-sorted-array/
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, cur = m-1, n-1, len(nums1)-1
        
        while i >= 0 or j >= 0:
            left = nums1[i] if i >= 0 else float('-inf')
            right = nums2[j] if j >= 0 else float('-inf')
            
            if left > right:
                nums1[cur] = left
                i -= 1
            else:
                nums1[cur] = right
                j -= 1
            cur -= 1
        