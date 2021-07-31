"""
Approach: backtracking

Status: Accepted
25 / 25 test cases passed.

Runtime: 24 ms
Memory Usage: 14.4 MB

Problem link: https://leetcode.com/problems/letter-combinations-of-a-phone-number
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit2char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        len_digits = len(digits)
        
        ans = []
        
        def bfs(i, str):
            if len(str) == len_digits:
                ans.append(str)
                return
                
            for c in digit2char[digits[i]]:
                bfs(i+1, str+c)
        
        if digits: bfs(0, "")
        
        return ans