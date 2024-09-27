class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=0
            a=nums[i]
            while a>0:
                s=(s*10)+(a%10)
                a=a//10
            nums.append(s)
        new_set=set(nums)
        return len(new_set)