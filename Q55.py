from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #solution1 TLE
        # n = len(nums)
        # if n == 0 or n==1:
        #     return True
        # isReachable = [False]*len(nums)
        # isReachable[0] = True
        # for i in range(1,n):
        #     for j in range(i):
        #         if nums[j]>=i-j and isReachable[j]:
        #             isReachable[i] = True
        # return isReachable[-1]

        #solution 2
        n = len(nums)
        if n==0 or n==0:
            return True
        isReachable = [False] * len(nums)
        isReachable[0] = True
        for i in range(n):
            if isReachable[i]:
                isReachable[i+1:i+nums[i]+1] = [True]*(nums[i])
        return isReachable[-1]

    #solution3:
    # m = 0
    # for i in range(len(n)-1):
    #     m = max(m, n[i] + i)
    #     if n[i] != 0: continue
    #     if m <= i: return False
    # return True


