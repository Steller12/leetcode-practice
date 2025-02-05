class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first=0
        second=0
        num=0
        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
                num+=1
                if num>2:
                    return False
                elif num==1:
                    first=i
                else:
                    second=i
        return (s1[first]==s2[second] and s1[second]==s2[first])