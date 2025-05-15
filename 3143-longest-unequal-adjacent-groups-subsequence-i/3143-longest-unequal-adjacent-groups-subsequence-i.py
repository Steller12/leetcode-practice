class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans=[]
        ans.append(words[0])
        for i in range(1,len(words)):
            if groups[i]==groups[i-1]:
                continue
            else:
                ans.append(words[i])
        return ans