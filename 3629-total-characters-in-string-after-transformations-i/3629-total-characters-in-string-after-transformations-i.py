class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod=10**9+7
        cnt=[0]*26
        for i in s:
            cnt[ord(i)-ord("a")]+=1
        for i in range(t):
            temp=[0]*26
            temp[0]=cnt[25]
            temp[1]=cnt[25]+cnt[0]
            for i in range(2,26):
                temp[i]=cnt[i-1]
            cnt=temp
        return sum(cnt)%mod