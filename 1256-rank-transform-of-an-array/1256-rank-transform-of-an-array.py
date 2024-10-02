class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(arr)
        d=defaultdict(int)
        r=1
        for i in range(len(a)):
            if a[i] not in d.keys():
                d[a[i]]=(r)
                r+=1
            else:
                continue
        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr