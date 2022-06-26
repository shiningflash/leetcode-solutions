class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map_nums = {}
        for x in nums:
            if x in map_nums:
                return x
            else:
                map_nums[x] = 1
