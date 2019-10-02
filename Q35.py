import bisect
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums,target,0,len(nums))

if __name__ == '__main__':
    print(Solution().searchInsert())
