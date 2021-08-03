"""
179 / 179 test cases passed.
Status: Accepted

Runtime: 12 ms
Memory Usage: 11.4 MB

Problem link: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
"""

class Solution {
public:
    bool makeEqual(vector<string>& words) {
        int len = words.size();
        vector <int> cnt(26, 0);
        for (int i = 0; i < len; i++) {
            int sz = words[i].length();
            for (int j = 0; j < sz; j++) {
                cnt[words[i][j]-'a']++;
            }
        }
        for (int i = 0; i < 26; i++) {
            if (cnt[i] % len != 0) {
                return false;
            }
        }
        return true;
    }
};