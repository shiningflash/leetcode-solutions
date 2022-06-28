class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowel(ch):
            return ch.lower() in ['a', 'e', 'i', 'o', 'u']
        
        all_vowel = [c for c in s if is_vowel(c)]
        ans_str = ""
        for c in s:
            if is_vowel(c):
                ans_str += all_vowel.pop()
                continue
            ans_str += c
        return ans_str
