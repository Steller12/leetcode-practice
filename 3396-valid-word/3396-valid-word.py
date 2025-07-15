class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vow=0
        cons=0
        vowels="aeiouAEIOU"
        for i in word:
            if i.isalpha():
                if i in vowels:
                    vow+=1
                else:
                    cons+=1
            elif not i.isdigit():
                return False
        if vow>=1 and cons>=1:
            return True
        else:
            return False