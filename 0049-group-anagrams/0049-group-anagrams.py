from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        result=[]
        
        for i in strs:
            s=tuple(sorted(i))
            dic[s].append(i)
        
        for i in dic.values():
            result.append(i)

        return result
