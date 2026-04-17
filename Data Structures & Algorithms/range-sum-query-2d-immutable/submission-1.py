class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix_mat = [[0 for _ in range(cols + 1)] for _ in range(rows+1)]

        for i in range(len(self.prefix_mat)):
            for j in range(len(self.prefix_mat[0])):
                if i == 0 or j == 0:
                    continue
                self.prefix_mat[i][j] = matrix[i-1][j-1] + self.prefix_mat[i-1][j] + self.prefix_mat[i][j-1] - self.prefix_mat[i-1][j-1]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1 + 1
        r2 = row2 + 1
        c1 = col1 + 1
        c2 = col2 + 1

        sum_region = self.prefix_mat[r2][c2] - self.prefix_mat[r1-1][c2] - self.prefix_mat[r2][c1-1] + self.prefix_mat[r1-1][c1-1]

        return sum_region
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)