"""
Status: Accepted

Problem link: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3974/
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = [ch for ch in s if ch.isalpha()]
        s = list(s)
        for pos in range(len(s)):
            if s[pos].isalpha():
                s[pos] = stack.pop()
        return "".join(s)