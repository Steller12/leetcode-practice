class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res=float('inf')
        for i in range(1,7):
            top=bot=0
            v=True
            for t,b in zip(tops,bottoms):
                if t!=i and b!=i:
                    v=False
                    break
                if t!=i:
                    top+=1
                if b!=i:
                    bot+=1
            if v:
                res=min(res,min(top,bot))
        if res==float('inf'):
            return -1
        else:
            return res