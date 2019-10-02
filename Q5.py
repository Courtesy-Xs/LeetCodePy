class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if(size<2):
            return s
        dp = [[False for i in range(size)] for i in range(size)]
        res = s[0]
        longest_s = 1

        for r in range(1,size):
            for l in range(r):
                if s[l]==s[r] and (r-l<=2 or dp[l+1][r-1]==True):
                    dp[l][r] = True
                    cur_len = r-l+1
                    if cur_len>longest_s:
                        longest_s = cur_len
                        res = s[l:r+1]
        return res


if __name__ == '__main__':
    s = "aaaa"
    Solution().longestPalindrome(s)