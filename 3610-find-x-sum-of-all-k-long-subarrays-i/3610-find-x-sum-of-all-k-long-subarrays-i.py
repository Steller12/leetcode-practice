class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n=len(nums)
        def x_sum(window):
            d={}
            for i in window:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
            freq=[(v,f) for v,f in d.items()]
            freq.sort(key = lambda t:(-t[1],-t[0]))
            total=0
            for j in range(min(x, len(freq))):
                total+=freq[j][0]*freq[j][1]
            return total
        ans=[]
        for i in range(n-k+1):
            window=nums[i:i+k]
            ans.append(x_sum(window))
        return ans
        