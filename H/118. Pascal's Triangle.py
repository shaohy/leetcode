class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = []
            row[0], row[-1] = [1, 1]
            for j in range(1,len(row)-1):
                row[j] = triangle[numRows-1][j-1] + triangle[numRows-1][j]
            triangle.append(row)
        return triangle

