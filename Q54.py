from typing import  List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        toL,toR,toU,toD = False,True,False,False
        left,right,top,bottom = 0,len(matrix[0]),0,len(matrix)
        count = 0
        resultList = []
        i,j = 0,0
        while count<len(matrix)*len(matrix[0]):
            resultList.append(matrix[i][j])
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
        return resultList

