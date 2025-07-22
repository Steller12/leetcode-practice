class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        d=dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        res=""
        for i,j in d.items():
            res+=i*j
        return res