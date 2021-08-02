"""
Approach: calculate xor and then return the number of set bit


149 / 149 test cases passed.
Status: Accepted

Runtime: 32 ms
Memory Usage: 14 MB

Problem link: https://leetcode.com/problems/hamming-distance/
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y; dis = 0
        
        while xor > 0:
            dis += (xor & 1)
            xor >>= 1
            
        return dis