class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merged(nums1.size()+nums2.size());
        merge(nums1.begin(),nums1.end(),nums2.begin(),nums2.end(),merged.begin());
        sort(merged.begin(),merged.end());
        int n=merged.size();
        if(n%2!=0){
            return (double)merged[n/2];
        }else{
            return (double)(merged[(n-1)/2]+merged[n/2])/2;
        }
    }
};