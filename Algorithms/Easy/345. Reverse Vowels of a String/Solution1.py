class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowel(ch):
            return ch.lower() in ['a', 'e', 'i', 'o', 'u']
        
        l = 0
        r = len(s) - 1
        s_list = list(s)
        
        while l < r:
            while l < r and not is_vowel(s[l]): l += 1
            while l < r and not is_vowel(s[r]): r -= 1
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
        return ''.join(s_list)
