class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        ans = []
        while i < len(word):
            c = 0
            curr = word[i]
            while i < len(word) and c < 9 and word[i] == curr:
                i = i + 1
                c = c + 1
            ans.append(str(c))
            ans.append(curr)
        return "".join(ans)
