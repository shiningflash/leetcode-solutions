/*
Approach: index mapping

171 / 171 test cases passed.
Status: Accepted

Runtime: 140 ms
Memory Usage: 85.2 MB

Problem link: https://leetcode.com/problems/first-missing-positive/
*/

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int mx = 500005, a[mx], len = nums.size();
        memset(a, 0, sizeof(a));
        for (int i = 0; i < len; i++) if (nums[i] > 0 && nums[i] < mx) a[nums[i]]++;
        for (int i = 1; i < mx; i++) if (a[i] == 0) return i;
        return 1;
    }
};