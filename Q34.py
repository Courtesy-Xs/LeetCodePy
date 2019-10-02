from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        resIndex = -1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                resIndex = mid
                break
        if resIndex is -1:
            return [-1,-1]
        else:
            s,e = resIndex,resIndex
            while s>-1 or e<len(nums):
                flag = True
                if s>-1 and nums[s] is target:
                    s-=1
                    flag = False
                if e<len(nums) and nums[e] is target:
                    e+=1
                    flag = False
                if flag:
                    break
            return [s+1,e-1]

if __name__ == '__main__':
    num = [2,2]
    print(Solution().searchRange(num,2))