class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp=[]
        for i,x in enumerate(nums):
            temp.append((x,i))
        temp.sort(reverse=True)
        return [info[0] for info in sorted(temp[:k], key=lambda info: info[1])]