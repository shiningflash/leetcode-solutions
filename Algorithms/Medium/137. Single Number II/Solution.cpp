/*
Approach: Bit Manipulation

14 / 14 test cases passed.
Status: Accepted

Runtime: 13 ms
Memory Usage: 9.5 MB

Problem link: https://leetcode.com/problems/single-number-ii
*/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            int bitsum = 0;
            for (int n : nums) bitsum += ((n >> i) & 1);
            res += (bitsum % 3 ? (1 << i) : 0);
        }
        return res;
    }
};