class Solution {
public:
    int countDigits(int num) {
        int dummy = num;
        int fac = 0;
        int ans = 0;
        while (dummy > 0) {
            fac = dummy % 10;
            dummy = dummy / 10;
            if (num % fac == 0) {
                ans += 1;
            }
        }
        return ans;
    }
};