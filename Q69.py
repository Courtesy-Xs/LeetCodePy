class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = 1,x
        mid = x
        while right>left:
            mid = (right+left)//2
            if mid**2==x:
                return mid
            if mid**2>x:
                right = mid-1
            else:
                left = mid+1
        if left**2>x:
            return left-1
        else:
            return left

if __name__ == '__main__':
    print(Solution().mySqrt(5))