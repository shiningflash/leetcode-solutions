class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_char = {}
        map_char_opp = {}
        for x, y in zip(s, t):
            if x not in map_char:
                if y in map_char_opp:
                    if x != map_char_opp[y]:
                        return False
                map_char[x] = y
                map_char_opp[y] = x
            else:
                if map_char[x] != y:
                    return False
        return True
        