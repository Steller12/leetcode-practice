class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d=defaultdict(int)
        c=0
        for i,j in dominoes:
            key=tuple(sorted((i,j)))
            c+=d[key]
            d[key]+=1
        return c