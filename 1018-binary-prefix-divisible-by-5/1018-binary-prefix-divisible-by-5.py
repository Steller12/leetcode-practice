class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        arr=[]
        arr.append(nums[0])
        ans=[]
        for i in range(1,len(nums)):
            arr.append((2*arr[i-1])+nums[i])
        for i in arr:
            if i%5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
