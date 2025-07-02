class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r=0, len(arr)-1
        while l<r:
            m=int((l+r)/2)
            mv=arr[m]
            lv=arr[m-1]
            rv=arr[m+1]
            if lv<mv:
                if rv<mv:
                    return m
                else:
                    l=m
            else:
                r=m