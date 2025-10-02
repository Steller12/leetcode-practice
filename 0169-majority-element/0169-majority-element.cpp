class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate, votes=0;
        for(int i=0;i<nums.size();i++){
            if(votes==0){
                votes=1;
                candidate=nums[i];
            }
            else{
                if(nums[i]==candidate){
                    votes++;
                }else{
                    votes--;
                }
            }
        }
            votes=0;
            for(int i=0;i<nums.size();i++){
                if(nums[i]==candidate){
                    votes++;
                }
            }
            if(votes>nums.size()/2){
                return candidate;
            }
            else{
                return -1;
            }
        
    }
};