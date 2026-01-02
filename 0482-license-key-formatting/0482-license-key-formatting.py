class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        x="".join(s.split("-")).upper()
        ans=[]
        for i in range(len(x),0,-k):
            ans.append(x[max(0,i-k):i])
        
        return "-".join(reversed(ans))