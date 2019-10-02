from typing import List

"""
"@ClassName:作于9.18生病
"@Description:TODO
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #solution1: 作于生病，累死了
        # """
        # Do not return anything, modify matrix in-place instead.
        # """
        # n = len(matrix)
        # if n<=1:
        #     return
        #
        # for i in range(int(n/2+0.5)):
        #     j,k = i,i
        #     tempList = []
        #     flag1 = True
        #     flag2 = False
        #     flag3 = False
        #     flag4 = True
        #     count = 0
        #     quantity = 4*(n-2*i)-4
        #     if not quantity:
        #         break
        #     if quantity==4:
        #         temp = [matrix[j+1][k],matrix[j][k],matrix[j][k+1],matrix[j+1][k+1]]
        #         matrix[j][k] = temp[0]
        #         matrix[j][k+1] = temp[1]
        #         matrix[j+1][k+1] = temp[2]
        #         matrix[j+1][k] = temp[3]
        #         break
        #     while count<quantity:
        #         tempList.append(matrix[j][k])
        #         count+=1
        #         if (count-1)%(n-2*i-1)==0:
        #             flag1 = not flag1
        #             flag2 = not flag2
        #         if count+1==2*(n-2*i):
        #             flag3 = not flag3
        #             flag4 = not flag4
        #         j+=flag1*(flag4-flag3)
        #         k+=flag2*(flag4-flag3)
        #     ix = (count+4)//4-1
        #     tempList = tempList[-ix:]+tempList[0:-ix]
        #     while count>0:
        #         matrix[j][k] = tempList.pop(0)
        #         count-=1
        #         if (count+1)%(n-2*i-1)==0:
        #             flag1 = not flag1
        #             flag2 = not flag2
        #             if ((count+1)//(n-2*i-1))%2==0:
        #                 flag3 = not flag3
        #                 flag4 = not flag4
        #
        #         j+=flag1*(flag4-flag3)
        #         k+=flag2*(flag4-flag3)
        # return
        return

if __name__ == '__main__':
    num1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    Solution().rotate(num1)
    print(num1)
