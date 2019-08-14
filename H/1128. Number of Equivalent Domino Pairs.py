from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        output = 0
        for i in range(len(dominoes)):
            a = dominoes[i]
            for j in range(i + 1, len(dominoes)):
                b = dominoes[j]
                if self.isdomino(a, b):
                    print(a, b)
                    output += 1
        return output

    def isdomino(self, a, b):
        return a == b or a[::-1] == b


test = Solution()
print(test.numEquivDominoPairs([[1, 2], [3, 3], [3, 3], [2, 1]]))
