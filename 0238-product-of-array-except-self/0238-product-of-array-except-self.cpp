class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans;
        int x=1;
        for(int i=0;i<nums.size();i++){
            if(i==0){
                ans.push_back(x);
            }
            else{
                x=x*nums[i-1];
                ans.push_back(x);
            }
        }
        x=1;
        for(int j=nums.size()-1;j>=0;j--){
            if(j==nums.size()-1){
                continue;
            }
            else{
                x=x*nums[j+1];
                ans[j]=ans[j]*x;
            }
        }
        return ans;
    }
};