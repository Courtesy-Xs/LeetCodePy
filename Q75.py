from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        L,R,i = 0,len(nums)-1,0
        while i < R+1:
            if nums[i] == 0:
                nums[i] = nums[L]
                nums[L] = 0
                L+=1
                i+=1
            elif nums[i] == 2:
                nums[i] = nums[R]
                nums[R] = 2
                R-=1
            else:
                i+=1

        #two-pass solution
        # count_0,count_1,count_2 = 0,0,0
        #
        # for val in nums:
        #     if val == 0:
        #         count_0+=1
        #     elif val == 1:
        #         count_1+=1
        #     else:
        #         count_2+=1
        # for i in range(len(nums)):
        #     if count_0:
        #         nums[i] = 0
        #         continue
        #     if count_1:
        #         nums[i] = 1
        #     if count_2:
        #         nums[i] = 2

if __name__ == '__main__':
    nums= [2,0,1,2,1,1,0,0,2]
    Solution().sortColors(nums)
    print(nums)
