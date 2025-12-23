class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        result = []
        mh = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(mh, (nums1[i] + nums2[0], i, 0))

        while k > 0 and mh:
            current_sum, i, j = heapq.heappop(mh)
            result.append((nums1[i], nums2[j]))
            k -= 1
            if j + 1 < len(nums2):
                heapq.heappush(mh, (nums1[i] + nums2[j + 1], i, j + 1))
        return result
