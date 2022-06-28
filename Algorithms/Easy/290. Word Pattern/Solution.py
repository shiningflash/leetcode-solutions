class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        map_word = {}
        map_word_rev = {}
        if len(pattern) != len(words):
            return False
        for key, word in zip(pattern, words):
            if key in map_word:
                if map_word[key] != word:
                    return False
            else:
                if word in map_word_rev:
                    if map_word_rev[word] != key:
                        return False
            map_word[key] = word
            map_word_rev[word] = key
        return True
