class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        while(x!=0):
            if x>0:
                pop = x%10
            else:
                pop = x%(-10)
            x /= 10
            x = int(x)
            if(rev>(2**31-1)/10) or (rev==(2**31-1)/10 and pop>7):
                return 0
            if(rev<-2**31/10) or (rev==-2**31/10 and pop<-8):
                return 0
            rev = rev*10 + pop
        return rev

if __name__ == '__main__':
    print(Solution().reverse(-123))