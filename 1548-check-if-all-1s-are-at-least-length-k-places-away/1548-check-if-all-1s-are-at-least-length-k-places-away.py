class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        distArray=[]
        x=None
        for i in range(len(nums)):
            if nums[i]==1:
                if x is not None:
                    distArray.append(i-x-1)
                x=i
        for i in distArray:
            if i<k:
                return False
        return True