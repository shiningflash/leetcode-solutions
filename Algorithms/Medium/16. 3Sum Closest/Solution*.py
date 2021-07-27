"""
Approach: Two Pointer

Status: Accepted
131 / 131 test cases passed.

Runtime: 120 ms
Memory Usage: 14.3 MB
"""

class Solution:
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dif, length = float('inf'), len(nums)
        
        for i in range(0, length-2):
            lo, hi = i+1, length-1
            while lo < hi:
                tsum = nums[i] + nums[lo] + nums[hi]
                if abs(target - tsum) < abs(dif):
                    dif = target - tsum
                if tsum < target:
                    lo += 1
                else:
                    hi -= 1
            if dif == 0:
                break
        return target - dif