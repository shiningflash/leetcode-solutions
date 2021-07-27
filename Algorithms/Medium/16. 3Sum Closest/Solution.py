"""
Approach: Binary Search

Status: Accepted
131 / 131 test cases passed.

Runtime: 640 ms
Memory Usage: 14.4 MB
"""

class Solution:
    
    def getClosest(self, val1: int, val2: int, x: int):
        if x - val1 >= val2 - x:
            return val2, val2-x
        else:
            return val1, x-val1
    
    def binarySearch(self, nums: int, length: int, start: int, x: int):
        if x <= nums[start]:
            return nums[start], nums[start]-x
        if x >= nums[length-1]:
            return nums[length-1], x-nums[length-1]

        i = start; j = length; mid = 0
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == x:
                return nums[mid], 0
            if nums[mid] > x:
                if mid > 0 and x > nums[mid-1]:
                    return self.getClosest(nums[mid-1], nums[mid], x)
                j = mid
            else:
                if mid < length-1 and x < nums[mid+1]:
                    return self.getClosest(nums[mid], nums[mid+1], x)
                i = mid+1
        return nums[mid], abs(x-nums[mid])
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        import math
        mn = math.inf
        ans = -1
        length = len(nums)
        for i in range(0, length - 2):
            for j in range(i+1, length-1):
                x = target - nums[i] - nums[j]
                new_x, dif = self.binarySearch(nums, length, j+1, x)
                if dif < mn:
                    mn = dif
                    ans = nums[i] + nums[j] + new_x
        return ans