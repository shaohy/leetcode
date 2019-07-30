class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        output = ""
        target = "aj"
        alpha_dic = {}
        start = (0, 0)  # a
        end = (1, 4)  # j
        for i in range(len(board)):
            for j in range(len(board[i])):
                alpha_dic[board[i][j]] = (i, j)
        print(alpha_dic)


test = Solution()
test.alphabetBoardPath("leet")