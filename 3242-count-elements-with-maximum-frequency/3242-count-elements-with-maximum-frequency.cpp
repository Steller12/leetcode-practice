class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int freq[101] = {0}, maxfreq = 0, res = 0;
        for (int n : nums) {
            freq[n] += 1;
            maxfreq = max(maxfreq, freq[n]);
        }
        for (int x : freq) {
            if (x == maxfreq) {
                res += x;
            }
        }
        return res;
    }
};