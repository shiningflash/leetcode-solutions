"""
Approach: Map with sorted words

114 / 114 test cases passed.
Status: Accepted

Runtime: 112 ms
Memory Usage: 17.3 MB

Problem link: https://leetcode.com/problems/group-anagrams/
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for word in strs:
            sort_word = "".join(map(str, sorted(word)))
            if not mydict.get(sort_word):
                mydict[sort_word] = list()
            mydict[sort_word].append(word)
        ans = []
        for key in mydict:
            ans.append(mydict[key])
        return ans
        