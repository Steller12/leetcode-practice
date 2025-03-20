class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        s=set(nums)
        ans=1
        for i in s:
            curr=1
            if i-1 in s:
                continue
            else:
                y=i
                while y+1 in s:
                    y=y+1
                    curr=curr+1
            ans=max(curr,ans)
        return ans
