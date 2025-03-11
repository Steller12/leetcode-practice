class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p=strs[0]
        n=len(p)
        for i in strs[1:]:
            while p!=i[0:n]:
                n=n-1
                if n == 0:
                    return ""
                p=p[0:n]
        return p