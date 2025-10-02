class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> numMap;
        for(int i=0; i<nums.size();i++){
            numMap[nums[i]]=i;
        }
        for(int i=0;i<nums.size();i++){
            int remaining=target-nums[i];
            if(numMap.count(remaining) && numMap[remaining]!=i){
                return {i,numMap[remaining]};
            }
        }
        return {};
    }
};