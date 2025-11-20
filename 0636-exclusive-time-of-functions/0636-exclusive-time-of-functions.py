class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        ans=[0]*n
        prev=0
        for i in logs:
            init, tp, time=i.split(":")
            init=int(init)
            time=int(time)
            if tp=="start":
                if stack:       
                    ans[stack[-1]]+=time-prev
                stack.append(init)
                prev=time
            else:
                ans[stack.pop()]+=time-prev+1
                prev=time+1
        return ans