from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for j in range(len(nums)-2,-1,-1):
            for i in range(len(nums)-1,j,-1):
                if nums[i]>nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    nums[j+1:] = sorted(nums[j+1:])
                    return None
                else:
                    continue
        nums.sort()
if __name__ == '__main__':
    nums = [4,2,0,2,3,2,0]
    Solution().nextPermutation(nums)
    print(nums)
