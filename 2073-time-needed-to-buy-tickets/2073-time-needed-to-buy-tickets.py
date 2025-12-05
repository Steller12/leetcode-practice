class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        temp=[(indx, i) for indx,i in enumerate(tickets)]
        ans=0
        while temp:
            i, val = temp.pop(0)
            val=val-1
            ans=ans+1
            if val==0:
                if i==k:
                    return ans
            else:
                temp.append((i, val))