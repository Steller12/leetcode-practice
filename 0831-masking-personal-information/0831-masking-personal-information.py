class Solution:
    def maskPII(self, s: str) -> str:
        def maskemail(s):
            s = s.lower()
            a = s.split('@')[0]
            b = s.split('@')[1]
            a = a[0]+'*'*5+a[-1]
            return a+'@'+b
        def maskphone(s):
            for x in '+-() ':
                s = s.replace(x, '')
    
            ln = len(s)
            res = ''
            if ln>10:
                res = '+'+'*'*(ln-10)+'-'
            res+='***-***-'+s[-4:]
            return res

        if "." in s:
            return maskemail(s)
        return maskphone(s)