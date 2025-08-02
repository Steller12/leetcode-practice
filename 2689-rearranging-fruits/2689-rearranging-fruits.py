class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        total=Counter(basket1)+Counter(basket2)
        for i in (total.values()):
            if i%2!=0:
                return -1
        to_swap=[]
        c1=Counter(basket1)
        for i,j in total.items():
            temp=j//2
            diff=c1.get(i,0)-temp
            for _ in range(abs(diff)):
                to_swap.append(i)
        to_swap.sort()
        ans=0
        helper=2*min(total.keys())
        for i in range(len(to_swap)//2):
            ans+=min(to_swap[i],helper)
        return ans