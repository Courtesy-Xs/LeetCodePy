from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        if len(nums) == 1:
            return nums[0]
        mid = self.chooseMid(nums)
        bigger = [i for i in nums if i >mid]
        smaller = [i for i in nums if i<mid]
        equal = [i for i in nums if i==mid]
        if len(bigger) < k <= len(bigger)+len(equal):
            return mid
        elif k<=len(bigger):
            return self.findKthLargest(bigger,k)
        else:
            return self.findKthLargest(smaller,k-len(equal)-len(bigger))

    def chooseMid(self,nums:List[int]):
        resList = []
        for i in range(len(nums)//5+1):
                tempList = nums[i*5:(i+1)*5]
                if len(tempList) == 5:
                    resList.append(sorted(tempList)[2])
                elif len(tempList) >0:
                    resList.append(sorted(tempList)[int(len(tempList)/2+0.5)-1])
                else:
                    break
        return self.findKthLargest(resList,len(resList)//2+1)

if __name__ == '__main__':
    len,k = input().split(" ")
    sArr = input().split()
    sArr = [int(i) for i in sArr]
    print(Solution().findKthLargest(sArr,k))






