class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}
        for x, y in zip(s, t):
            map_s[x] = 1 if x not in map_s else map_s[x]+1
            map_t[y] = 1 if y not in map_t else map_t[y]+1
        return map_s == map_t
        