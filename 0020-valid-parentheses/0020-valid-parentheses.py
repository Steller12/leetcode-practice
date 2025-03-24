class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                a.append(i)
            else:
                if not a:
                    return False
                elif i=='}' and a[-1]=='{':
                    a.pop()
                elif i==']' and a[-1]=='[':
                    a.pop()
                elif i==')' and a[-1]=='(':
                    a.pop()
                else:
                    return False
        if not a:
            return True
        else:
            return False