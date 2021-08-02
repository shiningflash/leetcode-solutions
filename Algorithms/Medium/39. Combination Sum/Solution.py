"""
Approach: backtracking


170 / 170 test cases passed.
Status: Accepted

Runtime: 100 ms
Memory Usage: 14.3 MB

Problem link: https://leetcode.com/problems/combination-sum
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        
        def backtrack(start, rem, arr = []):
            if rem < 0: return
            if rem == 0:
                ans.append(arr)
                return
            for pos in range(start, len(candidates)):
                backtrack(pos, rem - candidates[pos], arr + [candidates[pos]])
        
        backtrack(0, target)
        return ans