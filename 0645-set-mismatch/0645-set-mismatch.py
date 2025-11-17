class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        dup = -1
        miss = -1

        for key, val in d.items():
            if val == 2:
                dup = key
                break

        x = 1
        for key in sorted(d.keys()):
            if key != x:
                miss = x
                break
            x += 1

        if miss == -1:
            miss = x

        return [dup, miss]
