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
        map_paren = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = []
        for bracket in s:
            if bracket in map_paren: # if closing bracket
                # if stack empty, nothing to pop, so return False
                if not stack:
                    return False
                top = stack.pop()
                if map_paren[bracket] != top:
                    return False
            else:
                # for opening bracket, just append
                stack.append(bracket)
        # stack empty means valid parenthesis, otherwise not
        return not stack
