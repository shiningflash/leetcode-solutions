"""
Approach: Dynamic Programming


1146 / 1146 test cases passed.
Status: Accepted

Runtime: 188 ms
Memory Usage: 17.8 MB

Problem link: https://leetcode.com/problems/edit-distance/
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1) + 1, len(word2) + 1
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[m-1][n-1]