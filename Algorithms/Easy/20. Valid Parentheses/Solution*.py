"""
Approach: stack + map


91 / 91 test cases passed.
Status: Accepted

Runtime: 32 ms
Memory Usage: 14.1 MB

Problem link: https://leetcode.com/problems/valid-parentheses
"""

class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        stack = []
        for c in s:
            if c in mp:
                if not stack: return False
                top = stack.pop()
                if mp[c] != top: return False
            else:
                stack.append(c)
        return not stack