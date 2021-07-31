"""
Approach: stack

91 / 91 test cases passed.
Status: Accepted

Runtime: 32 ms
Memory Usage: 14.4 MB

Problem link: https://leetcode.com/problems/valid-parentheses
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
                continue
                
            if not stack: return False
            
            pop = stack.pop()
            if pop == '(' and c == ')':
                continue
            elif pop == '{' and c == '}':
                continue
            elif pop == '[' and c == ']':
                continue
            return False
        return not stack