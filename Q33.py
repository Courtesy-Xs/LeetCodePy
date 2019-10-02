from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        dict_nums = {j: i for i, j in enumerate(nums)}
        sortedNums = self.searchHelper(nums)
        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            if sortedNums[mid] > target:
                right = mid - 1
            elif sortedNums[mid] < target:
                left = mid + 1
            else:
                return dict_nums[sortedNums[mid]]
        # if sortedNums[left] is target:
        #     return dict_nums[sortedNums[left]]
        return -1

    def searchHelper(self, nums):
        left, right, mid = 0, len(nums) - 1, len(nums) // 2
        flag = False
        while right > left:
            if flag:
                break
            mid = (left + right) // 2
            if left is mid:
                flag = True
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1:] + nums[0:mid + 1]
            if nums[mid] >= nums[left]:
                left = mid
            else:
                right = mid
        return nums


if __name__ == '__main__':
    nums = [3,4,5,6,1,2]
    sortedNums = Solution().searchHelper(nums)
    print(sortedNums)
    print(Solution().search(nums, 2))
