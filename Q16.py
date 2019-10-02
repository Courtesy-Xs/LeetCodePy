from bisect import bisect_left
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #solution 1
        # nums, r, end = sorted(nums), float('inf'), len(nums) - 1
        # for c in range(len(nums) - 2):
        #     i, j = max(c + 1, bisect_left(nums, target - nums[end] - nums[c], c + 1, end) - 1), end
        #     while r != target and i < j:
        #         s = nums[c] + nums[i] + nums[j]
        #         r, i, j = min(r, s, key=lambda x: abs(x - target)), i + (s < target), j - (s > target)
        # return r



        #solution2
        nums.sort()
        ans = float("inf")

        for i in range(len(nums)-2):
            minSum = nums[i]+nums[i+1]+nums[i+2]
            maxSum = nums[i]+nums[-1]+nums[-2]
            left,right = i+1,len(nums)-1

            if minSum >= target:
                if abs(ans-target)<abs(minSum-target):
                    return ans
                return minSum
            if maxSum == target:
                return maxSum
            elif maxSum < target:
                if abs(maxSum-target) < abs(ans-target):
                    ans = maxSum
                continue
            else:
                while right > left:
                    temp = nums[i] + nums[left] + nums[right]
                    if abs(temp - target) < abs(ans - target):
                        ans = temp
                    if temp > target:
                        right-=1
                        while right > left and nums[right] == nums[right+1]:
                            right-=1
                    elif temp == target:
                        return temp
                    else:
                        left+=1
                        while right > left and nums[left-1] == nums[left]:
                            left+=1
        return ans






if __name__ == '__main__':
    arr = [0,2,1,-3]
    print(Solution().threeSumClosest(arr,1))