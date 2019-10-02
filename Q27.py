from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p,q = 0,0

        while q<len(nums):
            if nums[p] is val:
                if nums[q] is val:
                    q+=1
                else:
                    nums[p]=nums[q]
                    p+=1
                    nums[q]=val
                    q=p
            else:
                p+=1
                q=p
        return p

if __name__ == '__main__':
    nums = [3,2,2,3]
    print(Solution().removeElement(nums,3))
    print(nums)