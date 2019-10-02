from typing import List
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #quick pow
        if x == 0:
            return 0.0
        if n == 0:
            return 1.0
        if n < 0:
            x = 1/x
            n = -n

        r = 1
        while n:
            if n%2:
                r*=x
            n = n//2
            x*=x
        return r

if __name__ == '__main__':
    print(Solution().myPow(2,-2))
