class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        f=prices[0]
        for i in prices:
            if i<f:
                f=min(i,f)
            curr=i-f
            m=max(curr,m)
        return m