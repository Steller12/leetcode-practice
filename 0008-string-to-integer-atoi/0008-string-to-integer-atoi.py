class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        while i<len(s) and s[i]==' ':
            i+=1
        result=0
        sign=1
        if i<len(s) and (s[i]=='-' or s[i]=='+'):
            sign =-1 if s[i]=='-' else 1
            i+=1
        while i<len(s) and s[i].isdigit():
            result=result*10+int(s[i])
            if result*sign > 2**31 - 1:
                return 2**31 - 1
            elif result*sign< -2**31:
                return -2**31
            i+=1
        return result*sign