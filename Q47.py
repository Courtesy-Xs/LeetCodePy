from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #solution 2:
        return [[n]+p for n in set(nums) for p in self.permuteUnique(nums[:nums.index(n)]+nums[nums.index(n)+1:])] or [[]]


        #solution 1:
        # if len(nums)==1:
        #     return [nums]
        # resultList = []
        # def permuteHelper(result,remaining):
        #     if len(remaining)==1:
        #         if result+[remaining[0]] not in resultList:
        #             resultList.append(result+[remaining[0]])
        #         return
        #     else:
        #         for i in range(len(remaining)):
        #             permuteHelper(result+[remaining[i]],remaining[0:i]+remaining[i+1:])
        # for i in range(len(nums)):
        #     permuteHelper([nums[i]],nums[0:i]+nums[i+1:])
        # return resultList

if __name__ == '__main__':
    print(Solution().permuteUnique([]))
