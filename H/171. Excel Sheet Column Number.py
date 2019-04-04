class Solution:
    def titleToNumber(self, s: str) -> int:
        # if not s:
        #     return 0
        # return 26 * self.titleToNumber(s[:-1]) + ord(s[-1]) - 64

        result = 0
        for i in range(len(s)):
            result += (ord(s[i]) - 64) * 26 ** (len(s) - i - 1)
        return result