class Solution:
    def check(self, nums: List[int]) -> bool:
        flag=0
        count=0
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                flag=i
                count=count+1
        if count>1:
            return False
        if count==0:
            return True
        if count==1:
            if(nums[-1]<=nums[0]):
                return True
            else:
                return False