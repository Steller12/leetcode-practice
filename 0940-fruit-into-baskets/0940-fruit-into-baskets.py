class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start=0
        ans=0
        d=defaultdict(int)
        for end in range(len(fruits)):
            d[fruits[end]]+=1
            while len(d)>2:
                d[fruits[start]]-=1
                if d[fruits[start]]==0:
                    del d[fruits[start]]
                start+=1
            ans=max(ans,end-start+1)
        return ans