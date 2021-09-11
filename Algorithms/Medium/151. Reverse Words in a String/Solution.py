"""
57 / 57 test cases passed.
Status: Accepted

Runtime: 32 ms
Memory Usage: 14.4 MB

Problem link: https://leetcode.com/problems/reverse-words-in-a-string/
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = words[::-1]
        return " ".join(words)