class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=right=0
        total=0
        ans=float('inf')
        while right<len(nums) or total >= target:
            if total>=target:
                ans=min(ans,right-left)
                total-=nums[left]
                left+=1
            else:
                total+=nums[right]
                right+=1
        return 0 if ans == float('inf') else ans