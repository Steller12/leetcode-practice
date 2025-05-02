class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = list(dominoes)
        q = deque()
        for i, d in enumerate(dominoes):
            if d != ".":
                q.append((i, d))
        while q:
            i, d = q.popleft()
            if d == "L":
                if i > 0 and ans[i - 1] == ".":
                    ans[i - 1] = "L"
                    q.append((i - 1, "L"))
            elif d == "R":
                if i + 1 < len(ans) and ans[i + 1] == ".":
                    if i + 2 < len(ans) and ans[i + 2] == "L":
                        q.popleft()
                    else:
                        ans[i + 1] = "R"
                        q.append((i + 1, "R"))
        return "".join(ans)
