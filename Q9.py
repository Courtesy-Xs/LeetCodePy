
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s=str(x)
        # isPalindrome = True
        # for i in range(int(len(s)/2)):
        #     if s[i] != s[len(s)-i-1]:
        #         isPalindrome = False
        #
        # return isPalindrome
        s = list(str(x))
        s1 = s[:]
        s1.reverse()
        if s == s1:
            return True
        return False


if __name__ == '__main__':
    print(Solution().isPalindrome(1212))
