class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) >> 1
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if nums[low] < target:
            low += 1
        return low
