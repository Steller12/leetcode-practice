class Solution:
    def simplifyPath(self, path: str) -> str:
        x=path.split('/')
        stack=[]
        for i in x:
            if i:
                if i=="..":
                    if stack:
                        stack.pop()
                    else:
                        continue
                elif i==".":
                    continue
                else:
                    stack.append(i)
            else:
                continue
        return "/"+"/".join(stack)