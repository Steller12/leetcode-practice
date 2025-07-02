class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        x,m=0,0
        for i in range(len(arr)):
            if arr[i]>m:
                x=i
                m=arr[i]
        return x