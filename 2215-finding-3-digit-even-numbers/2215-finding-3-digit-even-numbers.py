class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        d={}
        res=[]
        for i in digits:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in range(100,999,2):
            h=i//100
            t=i//10 - h*10
            f=i%10
            
            d2={}
            d2[h]=1
            if t in d2:
                d2[t]+=1
            else:
                d2[t]=1
            if f in d2:
                d2[f]+=1
            else:
                d2[f]=1

            flag=True
            for k,m in d2.items():
                if d.get(k,0)<m:
                    flag=False
                    break
            
            if flag:
                res.append(i)
        return res

