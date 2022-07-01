class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        
        if not s or length < 1:
            return ""
        
        start = 0
        end = 0
        
        for i in range(length):
            len1 = self.expandPalindrom(s, length, i, i)
            len2 = self.expandPalindrom(s, length, i, i+1)
            max_len = max(len1, len2)
            if max_len > end - start + 1:
                start = i - ((max_len - 1) >> 1)
                end = i + (max_len >> 1)
        
        return s[start:end+1]
    
    def expandPalindrom(self, s: str, length: int, left: int, right: int) -> int:
        if left > right:
            return 0
        
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
            
        return right - left - 1
        