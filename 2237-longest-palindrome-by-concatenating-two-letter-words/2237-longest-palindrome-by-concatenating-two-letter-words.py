class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        counts = Counter(words)
        count = 0
        flag = False

        for word in list(counts.keys()):
            rev = word[::-1]
            if word == rev:
                count += (counts[word] // 2) * 4
                if counts[word] % 2 == 1:
                    flag = True
            elif rev in counts:
                matched = min(counts[word], counts[rev])
                count += matched * 4
                counts[word] = 0
                counts[rev] = 0

        return count + 2 if flag else count
