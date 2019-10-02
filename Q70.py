import math
class Solution:
    def climbStairs(self, n: int) -> int:
        #solution 1:
        # if n<=2:
        #     return n
        # return self.climbStairs(n-1)+self.climbStairs(n-2)

        #solution2:
        if n<=2:
            return n
        result = 1
        for i in range(1,n//2+1):
            result+=math.factorial(n-i*2+i)//(math.factorial(n-i*2)*math.factorial(i))
        return result

        #solution 3:
        # """
        # :type n: int
        # :rtype: int
        # """
        # steps = [1,1]
        # if n>=2:
        #     for i in range(2,n+1):
        #         steps.append(steps[i-1] + steps[i-2])
        # return steps[-1]

if __name__ == '__main__':
    print(Solution().climbStairs(3))