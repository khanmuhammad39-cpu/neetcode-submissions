class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)

        for i in range(rows):
            end_val = matrix[i][cols-1]
            if end_val < target:
                continue
            elif end_val == target:
                return True
            else:
                for j in range(cols):
                    val = matrix[i][j]
                    if val == target:
                        return True
        
        return False

        