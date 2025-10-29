class Solution {
public:
    int smallestNumber(int n) {
        int k = 1;
        int ans = 1;
        while (ans < n) {
            k = k + 1;
            ans = pow(2, k) - 1;
        }
        return ans;
    }
};