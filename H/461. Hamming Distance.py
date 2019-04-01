class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        new_x = bin(x)[2:]
        new_y = bin(y)[2:]
        new_x.rjust(max(len(new_x), len(new_y)), "0")
        new_y.rjust(len(new_x), "0")
        output = 0
        for i in range(len(new_x)):
            if new_x[i] != new_y[i]:
                output += 1
        return output
