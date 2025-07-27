class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        s=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                s.append(nums[i])
        ans=0
        for i in range(1, len(s)-1):
            if s[i]<s[i-1] and s[i]<s[i+1]:
                ans+=1
            elif s[i]>s[i-1] and s[i]>s[i+1]:
                ans+=1
            else:
                continue
        return ans