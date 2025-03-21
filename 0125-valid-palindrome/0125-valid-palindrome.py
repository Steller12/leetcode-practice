class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(ch.lower() for ch in s if ch.isalnum())
        l=0
        h=len(s)-1
        while l<h:
            if s[l]!=s[h]:
                return False
            l=l+1
            h=h-1

        return True