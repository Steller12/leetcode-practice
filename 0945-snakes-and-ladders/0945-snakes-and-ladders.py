class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        N = n * n
        dest = [0] * (N + 1)
        for s in range(1, N + 1):
            r = n - 1 - (s - 1) // n
            c = (s - 1) % n if ((s - 1) // n) % 2 == 0 else n - 1 - (s - 1) % n
            dest[s] = board[r][c] if board[r][c] != -1 else s

        dist = [-1] * (N + 1)
        dist[1] = 0
        q = deque([1])
        while q:
            s = q.popleft()
            for i in range(1, 7):
                nxt = s + i
                if nxt > N: break
                d2 = dest[nxt]
                if dist[d2] == -1:
                    dist[d2] = dist[s] + 1
                    if d2 == N: return dist[N]
                    q.append(d2)

        return dist[N]