class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int curr=Integer.MAX_VALUE;
        for(int a : nums){
            if (curr==a){
                return true;
            }
            curr=a;
        }
        return false;
    }
}