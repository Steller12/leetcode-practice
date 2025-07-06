class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1=nums1
        self.n2=nums2
        self.freq2=Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old=self.n2[index]
        new=old+val
        self.freq2[old]-=1
        if self.freq2[old]==0:
            del self.freq2[old]
        self.freq2[new]+=1
        self.n2[index]=new

    def count(self, tot: int) -> int:
        d=Counter(self.n1)
        ans=0
        for i in d:
            ans+=d[i]*self.freq2.get(tot-i,0)
            
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)