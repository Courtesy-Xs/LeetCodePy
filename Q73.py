from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRows = set()
        zeroColumns = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    continue
                else:
                    zeroRows.add(i)
                    zeroColumns.add(j)
        for val in zeroRows:
            matrix[val][:] = [0]*n
        for val in zeroColumns:
            for k in range(m):
                matrix[k][val] = 0

if __name__ == '__main__':
    matrix = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    Solution().setZeroes(matrix)
    print(matrix)