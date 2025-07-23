class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(s, a, b, val):
            stack=[]
            ans=0
            for i in s:
                if stack and stack[-1]==a and i==b:
                    stack.pop()
                    ans+=val
                else:
                    stack.append(i)
            return ''.join(stack),ans
        if x>y:
            s, first=remove(s, 'a', 'b', x)
            s, second=remove(s,'b','a',y)
        else:
            s, first=remove(s, 'b', 'a', y)
            s, second=remove(s,'a','b',x)
        return first+second