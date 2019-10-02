from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxVal = 0
        while j>i:
            tempVal = (j-i)*min(height[i],height[j])
            if maxVal < tempVal:
                maxVal = tempVal
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return maxVal
