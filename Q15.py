from itertools import combinations
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # D,S = {j:i for i,j in enumerate(nums)},set()
        # for [(a,i),(b,j)] in combinations(zip(nums,range(len(nums))),2):
        #     if -(a+b) in D and  D[-(a+b)] >j:                        #D[-(a+b)]!=i and D[-(a+b)]!=j:此处这样的判断会导致重复的答案，自己思考
        #         S.add((a,b,-(a+b)))
        # return S

        # another Solution
        # P,N,Z = [],[],[]
        # S = set()
        # for n in nums:
        #     if n>0:
        #         P.append(n)
        #     elif n==0:
        #         Z.append(n)
        #     else:
        #         N.append(n)
        # if len(Z) >= 3:
        #     S.add((0,0,0))
        # if len(Z) >= 1:
        #     for a in P:
        #         if -a in N:
        #             S.add((a,-a,0))
        # judgeSet = set()
        # for (a,b) in combinations(P,2):
        #     if (b,a) in judgeSet or (a,b) in judgeSet:
        #         continue
        #     else:
        #         judgeSet.add((a,b))
        #         judgeSet.add((b,a))
        #     if -(a+b) in N:
        #         S.add((a,b,-(a+b)))
        # for (a,b) in combinations(N,2):
        #     if (b,a) in judgeSet or (a,b) in judgeSet:
        #         continue
        #     else:
        #         judgeSet.add((a,b))
        #         judgeSet.add((b,a))
        #     if -(a+b) in P:
        #         S.add((a,b,-(a+b)))
        # return S

        #solution 3:
        nums.sort()
        N,S = [[],[],0,0,[]],set()
        for i in nums: N[(i>0)-(i<0)].append(i)
        for i in [1,-1]: N[2*i] = set(N[-i])
        if len(N[0]) >= 3: S.add((0,0,0))
        if len(N[0]) != 0:
            for i in N[1]:
                if -i in N[2]: S.add((i,0,-i))
        for i in [1,-1]:
            for [a,b] in combinations(N[i],2):
                if -(a+b) in N[2*i]: S.add((a,b,-(a+b)))
        return S


if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,0]))
