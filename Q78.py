from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for j  in range(len(nums)):
            res.extend([val+[nums[j]] for val in res])
        return res





if __name__ == '__main__':
    print(Solution().subsets([1,2,3]))


