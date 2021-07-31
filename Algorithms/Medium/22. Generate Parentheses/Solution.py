"""
Approach: backtracking

8 / 8 test cases passed.
Status: Accepted

Runtime: 36 ms
Memory Usage: 14.5 MB

Problem link: https://leetcode.com/problems/generate-parentheses/
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(str = "", p_open = 0, p_close = 0):
            if len(str) == 2*n:
                res.append(str)
                return
            if p_open < n:
                backtrack(str + '(', p_open+1, p_close)
            if p_close < p_open:
                backtrack(str + ')', p_open, p_close+1)
            
        backtrack()
        return res
        