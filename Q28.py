class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1

        if len(needle) is 0:
            return 0
        if len(haystack) is 0:
            return -1

        p=0
        while len(haystack)-p+1>len(needle):
            if haystack[p]!=needle[0]:
                p+=1
            else:
                flag = True
                for i in range(len(needle)):
                    if haystack[p+i]!=needle[i]:
                        flag = False
                        break
                if flag:
                    return p
                else:
                    p+=1
        return -1