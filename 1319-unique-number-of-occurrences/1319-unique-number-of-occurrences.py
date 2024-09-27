class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=defaultdict(int)
        s=set()
        for i in range(len(arr)):
            d[arr[i]]+=1
        for val in d.values():
            if val in s:
                return False
            else:
                s.add(val)
        return True
