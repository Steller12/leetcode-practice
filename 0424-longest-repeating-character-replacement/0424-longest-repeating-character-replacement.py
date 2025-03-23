class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        d={}
        ans=0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=0
            d[s[i]]+=1
            if len(s[l:i])+1-max(d.values())<=k:
                ans=max(ans, len(s[l:i])+1)
            else:
                d[s[l]]-=1
                if not d[s[l]]:
                    d.pop(s[l])
                l=l+1
        return ans