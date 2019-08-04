class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        target = "a" + target
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        output = ""
        alpha_dic = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                alpha_dic[board[i][j]] = (i, j)

        for i in range(len(target) - 1):

            if alpha_dic[target[i]][0] > alpha_dic[target[i + 1]][0]:
                output += "U" * abs(alpha_dic[target[i]][0] - alpha_dic[target[i + 1]][0])
            if alpha_dic[target[i]][0] < alpha_dic[target[i + 1]][0]:
                output += "D" * abs(alpha_dic[target[i]][0] - alpha_dic[target[i + 1]][0])
            if alpha_dic[target[i]][0] > alpha_dic[target[i + 1]][0]:
                output += "R" * abs(alpha_dic[target[i]][1] - alpha_dic[target[i + 1]][1])
            if alpha_dic[target[i]][0] < alpha_dic[target[i + 1]][0]:
                output += "L" * abs(alpha_dic[target[i]][1] - alpha_dic[target[i + 1]][1])
            output += "!"
        return output


test = Solution()
print(test.alphabetBoardPath("leet"))
