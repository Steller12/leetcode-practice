class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]]+=1
        for i in d.values():
            if i>1:
                return True
        return False