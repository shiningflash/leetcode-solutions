class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len11 = len(text1)
        len21 = len(text2)
        dp = [[0 for _ in range(len11+1)] for _ in range(len21+1)]
        for i in range(1, len21+1):
            for j in range(1, len11+1):
                dp[i][j] = 1 + dp[i-1][j-1] if text2[i-1] == text1[j-1] else max(dp[i-1][j], dp[i][j-1])
        return dp[len21][len11]
