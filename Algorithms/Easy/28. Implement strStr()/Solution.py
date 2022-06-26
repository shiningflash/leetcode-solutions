class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)
        
        if len_needle > len_haystack:
            return -1
        if len_needle == 0:
            return 0
        
        def check_substr(pos_hays: int) -> bool:
            for curr_needle in needle:
                if curr_needle != haystack[pos_hays]:
                    return False
                pos_hays += 1
            return True
        
        for pos_haystack in range(len_haystack-len_needle+1):
            found = check_substr(pos_haystack)
            if found:
                return pos_haystack
        return -1
