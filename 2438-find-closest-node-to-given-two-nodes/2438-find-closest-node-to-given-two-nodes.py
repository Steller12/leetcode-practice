class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dist(start):
            n = len(edges)
            arr = [-1] * n
            cur = start
            d = 0
            while cur != -1 and arr[cur] == -1:
                arr[cur] = d
                d += 1
                cur = edges[cur]
            return arr

        dist1 = dist(node1)
        dist2 = dist(node2)

        ans = -1
        minn = float('inf')
        
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                maxx = max(dist1[i], dist2[i])
                if maxx < minn:
                    minn = maxx
                    ans = i
                elif maxx == minn and i < ans:
                    ans = i
        
        return ans