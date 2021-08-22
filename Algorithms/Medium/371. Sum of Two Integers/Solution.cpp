/*
Approach: AND, XOR

13 / 13 test cases passed.
Status: Accepted

Runtime: 0 ms
Memory Usage: 6 MB

Problem link: https://leetcode.com/problems/sum-of-two-integers/
*/

class Solution {
public:
    int getSum(int a, int b) {
        while (b) {
            unsigned c = a & b; // carry value
            a = a ^ b; // xor value
            b = c << 1; // shift carry value
        }
        return a;
    }
};