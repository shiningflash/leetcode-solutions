class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_magazine = {}
        for c in magazine:
            map_magazine[c] = 1 if c not in map_magazine else map_magazine[c] + 1
        for x in ransomNote:
            if x not in map_magazine:
                return False
            else:
                if map_magazine[x] < 1:
                    return False
            map_magazine[x] -= 1
        return True
