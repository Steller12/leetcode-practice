class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr_max=0
        l=0
        h=len(height)-1
        while l<h:
            curr_max=max(curr_max,(min(height[l],height[h])*(h-l)))
            if height[l]<height[h]:
                l=l+1
            else:
                h=h-1
        return curr_max
            
