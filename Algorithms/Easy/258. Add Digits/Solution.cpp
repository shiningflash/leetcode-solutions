class Solution {
public:
    int sumOfDigit(int n) {
        int sum = 0;
        while (n > 0) {
            sum += (n % 10);
            n /= 10;
        }
        return sum;
    }
    int addDigits(int num) {
        while (true) {
            if (num / 10 == 0) return num;
            else num = sumOfDigit(num);
        }
    }
};