from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        N = list(range(len(S) + 1))
        A = []
        for i in S:
            if i == "I":
                A.append(N.pop(0))
            else:
                A.append(N.pop())
        A.append(N.pop())
        return A


