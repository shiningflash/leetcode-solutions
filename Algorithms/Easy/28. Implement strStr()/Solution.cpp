class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.length(), m = needle.length();
        if (m > n) return -1;
        if (m == 0) return 0;
        for (int i = 0; i < n; i++) {
            bool f = true;
            for (int j = 0, p = i; j < m; j++) {
                if (haystack[p++] != needle[j]) { f = false; break; }
                if (i+j >= n) return -1;
            }
            if (f) return i;
        }
        return -1;
    }
};