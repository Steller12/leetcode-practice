class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr=sorted([j for i in grid for j in i])
        ans=0
        rem=arr[0]%x
        m=arr[len(arr)//2]
        
        for i in arr:
            if i%x!=rem:
                return -1
            ans=ans+abs(i-m)//x
        return ans