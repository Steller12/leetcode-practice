class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s=set()
        count=0
        for i in range(len(words)):
            if words[i][::-1] in s:
                count+=1
            else:
                s.add(words[i])
        return count