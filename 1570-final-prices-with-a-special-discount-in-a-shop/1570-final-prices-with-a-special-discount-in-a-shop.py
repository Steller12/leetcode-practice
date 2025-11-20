class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        for i in range(len(prices)):
            x=prices[i]
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    x=prices[i]-prices[j]
                    break
            ans.append(x)
        return ans