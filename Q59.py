from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==0:
            return [[]]
        result = [[0 for i in range(n)] for i in range(n)]
        toL,toR,toU,toD = False,True,False,False
        left,right,top,bottom = 0,n,0,n
        count = 0
        i,j = 0,0
        while count<n*n:
            result[i][j] = count+1
            count+=1
            i+=toD
            i-=toU
            j+=toR
            j-=toL
            if j>right-1:
                j-=1
                i+=1
                toR = False
                toD = True
                top+=1
                continue
            if i>bottom-1:
                i-=1
                j-=1
                toD = False
                toL = True
                right-=1
                continue
            if j<left:
                j+=1
                i-=1
                toL = False
                toU = True
                bottom-=1
                continue
            if i<top:
                i+=1
                j+=1
                toU = False
                toR = True
                left+=1
                continue
        return result

if __name__ == '__main__':
    print(Solution().generateMatrix(3))