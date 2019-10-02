from typing import List
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        resultList = []
        def permuteHelper(result,remaining):
            if len(remaining)==1:
                resultList.append(result+[remaining[0]])
                return
            else:
                for i in range(len(remaining)):
                    permuteHelper(result+[remaining[i]],remaining[0:i]+remaining[i+1:])
        for i in range(len(nums)):
            permuteHelper([nums[i]],nums[0:i]+nums[i+1:])
        return resultList


if __name__ == '__main__':
    print(len(Solution().permute([1])))






