from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #solution 1:
        # def helper(arr):
        #     m = len(arr)
        #     n = len(arr[0])
        #     downPart,rightPart = 0,0
        #     if m==1 and n==1:
        #         return 1
        #     if m>1 and (not arr[1][0]):
        #         downPart = helper(arr[1:][:])
        #     if n>1 and (not arr[0][1]):
        #         rightPart = helper([i[1:] for i in arr])
        #     return rightPart+downPart
        # m = len(obstacleGrid)
        # if m==0:
        #     return 0
        # n = len(obstacleGrid[0])
        # if obstacleGrid[0][0]==1:
        #     return 0
        # return helper(obstacleGrid)

        #solution2:
        m = len(obstacleGrid)
        if m==0:
            return 0
        n = len(obstacleGrid[0])
        helperMat = [[0 for i in range(n)] for j in range(m)]
        helperMat[0][0] = 1-obstacleGrid[0][0]
        for i in range(m):
            for j in range(n):
                upPart,leftPart=0,0
                if i==0 and j==0:
                    continue
                if not obstacleGrid[i][j]:
                    if i-1>=0:
                        upPart = helperMat[i-1][j]
                    if j-1>=0:
                        leftPart = helperMat[i][j-1]
                    helperMat[i][j] = leftPart+upPart
                else:
                    helperMat[i][j] = 0
        return helperMat[-1][-1]



if __name__ == '__main__':
    arr = [[1,0,0],[0,1,0],[0,0,0]]
    print(Solution().uniquePathsWithObstacles(arr))










