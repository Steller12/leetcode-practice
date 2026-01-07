class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        copy=s
        x=len(s)
        for i in range(x):
            copy=copy[-1]+copy[:x-1]
            if copy==goal:
                return True
        return False