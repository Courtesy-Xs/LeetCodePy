class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        p=0
        max = 0
        while(p<length and max < length - p):
            q=p
            tempLen = 0
            strSet = set()
            while(q<length):
                if s[q:q+1] in strSet:
                    break
                else:
                    strSet.add(s[q:q+1])
                    q+=1
                    tempLen+=1
            if max<tempLen:
                max = tempLen
            p+=1
        return max


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("adfgdfhgad"))
