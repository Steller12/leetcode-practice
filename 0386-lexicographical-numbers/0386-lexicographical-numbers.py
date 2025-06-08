class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        self.ans = []

        def solve(i):
            if i > n:
                return
            cur = i 
            self.ans.append(cur)
            for i in range(10):
                tmp = cur * 10 + i
                solve(tmp)

        for i in range(1, 10):
            solve(i)

        return self.ans