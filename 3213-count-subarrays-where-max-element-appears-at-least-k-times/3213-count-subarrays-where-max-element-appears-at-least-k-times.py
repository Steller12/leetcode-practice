class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l=0
        window=0
        element=max(nums)
        ans=0
        for r in range(l,len(nums)):
            if nums[r]==element:
                window+=1
            while window>=k:
                if nums[l]==element:
                    window-=1
                l+=1
            ans+=l
        return ans