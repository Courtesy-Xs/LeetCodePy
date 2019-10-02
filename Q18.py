from itertools import  combinations
import  collections
from typing import  List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Solution 1:
        # nums.sort()
        # resultSet = set()
        # for [(a,i),(b,j),(c,k)] in combinations(zip(nums,range(len(nums))),3):
        #     if target-(a+b+c) in nums[k+1:]:
        #         resultSet.add((a,b,c,target-(a+b+c)))
        # return [list(ele) for ele in resultSet]

        #Solution 2:
        #二重循环+hash表映射 用内存换时间
        # dic, l = collections.defaultdict(list), [*combinations(range(len(nums)), 2)]
        # for a, b in l: dic[target - nums[a] - nums[b]].append((a, b))
        # r = [(*ab, c, d) for c, d in l for ab in dic[nums[c] + nums[d]]]
        # return [*set(tuple(sorted(nums[i] for i in t)) for t in r if len(set(t)) == 4)]

        #solution 3:
        # nums.sort()
        # L,S = len(nums),set()
        # for i in range(L-3):
        #     maxVal = nums[i]+nums[-1]+nums[-2]+nums[-3]
        #     minVal = nums[i]+nums[i+1]+nums[i+2]+nums[i+3]
        #     if maxVal<target:
        #         continue
        #     if minVal>target:
        #         break
        #     for j in range(i+1,L-2):
        #         maxVal = nums[i]+nums[j]+nums[-1]+nums[-2]
        #         minVal = nums[i]+nums[j]+nums[j+1]+nums[j+2]
        #         if maxVal<target:
        #             continue
        #         if minVal>target:
        #             break
        #         left = j+1
        #         right = L-1
        #         while right>left:
        #             tempSum = nums[i]+nums[j]+nums[left]+nums[right]
        #             if tempSum>target:
        #                 right-=1
        #                 while right>left+1 and nums[right]==nums[right+1]:
        #                     right-=1
        #             elif tempSum==target:
        #                 S.add((nums[i],nums[j],nums[left],nums[right]))
        #                 left+=1
        #                 right-=1
        #             else:
        #                 left+=1
        #                 while right>left+1 and nums[left-1]==nums[left]:
        #                     left+=1
        # return S

        #Solution 4:
        nums.sort()
        L,N,S,M = len(nums),{j:i for i,j in enumerate(nums)},set(),nums[-1]
        for i in range(L-3):
            a = nums[i]
            if a + 3*M < target: continue
            if 4*a > target: break
            for j in range(i+1,L-2):
                b = nums[j]
                if a + b + 2*M < target: continue
                if a + 3*b > target: break
                for k in range(j+1,L-1):
                    c = nums[k]
                    d = target-(a+b+c)
                    if d > M: continue
                    if d < c: break
                    if d in N and N[d] > k: S.add((a,b,c,d))
        return S




if __name__ == '__main__':
    print(len(Solution().fourSum([-5,-4,-3,-2,-1,0,0,1,2,3,4,5],0)))
