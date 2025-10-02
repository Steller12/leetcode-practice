class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int s= nums.size();
        vector<int> num2(s*2,0);
        for(int i=0; i<s; i++){
            num2[i]=nums[i];
            num2[i+s]=nums[i];
        }
        return num2;
    }
};