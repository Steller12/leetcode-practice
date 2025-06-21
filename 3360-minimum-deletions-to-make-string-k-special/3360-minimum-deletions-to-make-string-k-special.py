class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        dic=defaultdict()
        for i in word:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        res=len(word)
        for i in dic.values():
            temp=0
            for j in dic.values():
                if j<i:
                    temp+=j
                if j>i+k:
                    temp+=j-(i+k)
            res=min(res,temp)
        return res
