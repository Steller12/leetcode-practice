from itertools import product

class Solution:
    def colorTheGrid(self, m, n):
        MOD = 10**9 + 7

        def is_valid(row):
            for i in range(len(row) - 1):
                if row[i] == row[i+1]:
                    return False
            return True

        all_patterns = [p for p in product((0, 1, 2), repeat=m) if is_valid(p)]
        pattern_index = {p: i for i, p in enumerate(all_patterns)}

        compatible = [[] for _ in all_patterns]
        for i, a in enumerate(all_patterns):
            for j, b in enumerate(all_patterns):
                if all(a[k] != b[k] for k in range(m)):
                    compatible[i].append(j)

        dp = [1] * len(all_patterns)
        for _ in range(1, n):
            new_dp = [0] * len(all_patterns)
            for i in range(len(all_patterns)):
                for j in compatible[i]:
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD