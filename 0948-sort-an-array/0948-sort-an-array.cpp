class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        mergesort(nums, 0, nums.size() - 1);
        return nums;
    }

private:
    void mergesort(vector<int>& nums, int L, int R) {
        if (L >= R) {
            return;
        }
        int m = (L + R) / 2;
        mergesort(nums, L, m);
        mergesort(nums, m + 1, R);
        merge(nums, L, m, R);
    }
    void merge(vector<int>& nums, int L, int m, int R) {
        vector<int> temp;
        int i = L, j = m + 1;
        while (i <= m && j <= R) {
            if (nums[i] <= nums[j]) {
                temp.push_back(nums[i++]);
            } else {
                temp.push_back(nums[j++]);
            }
        }
        while (i <= m) {
            temp.push_back(nums[i++]);
        }
        while (j <= R) {
            temp.push_back(nums[j++]);
        }
        for (int i = 0; i < temp.size(); i++) {
            nums[L + i] = temp[i];
        }
    }
};