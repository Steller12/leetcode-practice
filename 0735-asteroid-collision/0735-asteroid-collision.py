class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            while stack and i<0<stack[-1]:
                c=i+stack[-1]
                if c>0:
                    i=0
                elif c<0:
                    stack.pop()
                else:
                    stack.pop()
                    i=0
            if i:
                stack.append(i)
        return stack