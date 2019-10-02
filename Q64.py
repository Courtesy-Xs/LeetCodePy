from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #solution 1
        # m = len(grid)
        # if m==0:
        #     return 0
        # n = len(grid[0])
        # helperMat = [[0 for i in range(n)] for j in range(m)]
        # helperMat[0][0] = grid[0][0]
        #
        # for i in range(m):
        #     for j in range(n):
        #         upperPart,leftPart = float("inf"),float("inf")
        #         if i==0 and j==0:
        #             continue
        #         if i-1>=0:
        #             upperPart = helperMat[i-1][j]
        #         if j-1>=0:
        #             leftPart = helperMat[i][j-1]
        #         helperMat[i][j] = grid[i][j]+min(upperPart,leftPart)
        # return helperMat[-1][-1]
        #solution2:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = (min(dp[j], dp[j-1]) or dp[j-1]) + grid[i][j]
        return dp[-1]

if __name__ == '__main__':
    nums = [[1,3,1],[1,5,1],[4,2,1]]
    print(Solution().minPathSum(nums))

        