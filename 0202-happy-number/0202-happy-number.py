class Solution:
    def isHappy(self, n: int) -> bool:
        arr=[]
        res=0
        while n!=1:
            while n:
                res += (n%10)**2
                n=n//10
            arr.append(res)
            arr.sort()
            n=res
            res=0
            for i in range(1,len(arr)):
                if arr[i-1]==arr[i]:
                    return False
        return True