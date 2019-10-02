from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) is 1:
            return 1


        p,q = 0,1
        while q<len(nums):
            if nums[p]<nums[q]:
                if q-p>1:
                    p+=1
                    nums[p]=nums[q]
                else:
                    p+=1
                    q+=1
            else:
                q+=1
        return p+1

if __name__ == '__main__':
    nums = [0,0,1,1,2,3,4,5]
    print(Solution().removeDuplicates(nums))
    print(nums)