class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        target = "a" + target
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        output = ""
        alpha_dic = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                alpha_dic[board[i][j]] = (i, j)
        print(alpha_dic)

        for i in range(len(target) - 1):
            a = target[i]
<<<<<<< HEAD
            b = target[i + 1]
            if a == b:
                output += "!"
                continue

            if b == "z":
                b = "u"

=======
            b = target[i+1]
            if a == b:
                output += "!"
                continue
            if target[i+1] == "z":
                b = "u"

>>>>>>> 6127b870e67808aed1d3988ad681119ccb600b77
            if alpha_dic[a][0] > alpha_dic[b][0]:
                output += "U" * abs(alpha_dic[a][0] - alpha_dic[b][0])
            if alpha_dic[a][0] < alpha_dic[b][0]:
                output += "D" * abs(alpha_dic[a][0] - alpha_dic[b][0])
            if alpha_dic[a][1] > alpha_dic[b][1]:
                output += "L" * abs(alpha_dic[a][1] - alpha_dic[b][1])
            if alpha_dic[a][1] < alpha_dic[b][1]:
                output += "R" * abs(alpha_dic[a][1] - alpha_dic[b][1])

            if target[i + 1] == "z":
=======
            if target[i+1] == "z":
>>>>>>> 6127b870e67808aed1d3988ad681119ccb600b77
                output += "D"
            output += "!"
        return output


test = Solution()
print(test.alphabetBoardPath("zzz"))
print(test.alphabetBoardPath("leet"))
print(test.alphabetBoardPath("zdz"))
print(test.alphabetBoardPath("zz"))
