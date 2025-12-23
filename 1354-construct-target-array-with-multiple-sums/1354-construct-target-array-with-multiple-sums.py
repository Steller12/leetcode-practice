class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        total = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)

        while True:
            max_element = -heapq.heappop(target)
            remaining = total - max_element

            if max_element == 1 or remaining == 1:
                return True

            if remaining == 0 or max_element <= remaining:
                return False

            max_element %= remaining
            if max_element == 0:
                return False

            total = remaining + max_element
            heapq.heappush(target, -max_element)
