class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> myMap;
        for (int i = 0; i < nums.size(); i++) {
            myMap[nums[i]] += 1;
        }
        vector<vector<int>> counter(nums.size() + 1);
        for (auto& pair : myMap) {
            counter[pair.second].push_back(pair.first);
        }
        vector<int> res;
        for (int i = counter.size() - 1; i >= 0; i--) {
            for (int num : counter[i]) {
                res.push_back(num);
                if (res.size() == k) {
                    return res;
                }
            }
        }
        return {};
    }
};