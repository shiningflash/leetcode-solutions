class Solution:
    def compare(self, x: str, y: str):
        if x+y > y+x:
            return x, y
        return y, x
    
    def custom_sort(self, nums) -> str:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                nums[i], nums[j] = self.compare(nums[i], nums[j])
        return ''.join(nums)
    
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        ans = self.custom_sort(nums)
        return "0" if ans[0]=="0" else ans
        