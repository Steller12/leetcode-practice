class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<=r:
            mid=(l+r)//2
            ans=0
            for i in piles:
                ans+=(i+mid-1)//mid
            if ans>h: l=mid+1
            else: r=mid-1
        return l