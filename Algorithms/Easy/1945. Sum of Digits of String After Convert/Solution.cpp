class Solution {
public:
    long long charToInt(char c) {
        return c - 'a' + 1;
    }
    
    int sumOfDigit(long long n) {
        int sum = 0;
        while (n > 0) {
            sum += (n % 10);
            n /= 10;
        }
        return sum;
    }
    
    int strToInt(string s) {
        int sum = 0;
        for (auto &c : s) {
            sum += sumOfDigit(charToInt(c));
        }
        return sum;
    }
    
    int getLucky(string s, int k) {
        int num = strToInt(s);
        for (int i = 0; i < k-1; i++) {
            num = sumOfDigit(num);
        }
        return num;
    }
};