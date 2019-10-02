class Solution:
    def simplifyPath(self, path: str) -> str:
        #wrong for test case /...
        # result = []
        # i,n = 1,len(path)
        #
        # while i<n:
        #     preC = path[i-1]
        #     nowC = path[i]
        #     if preC.isalnum():
        #         temp = ""
        #         while path[i-1].isalnum():
        #             temp+=path[i-1]
        #             i+=1
        #         result.append(temp)
        #     else:
        #         if preC == "/":
        #             while i<n+1 and path[i-1] == "/":
        #                 i+=1
        #             continue
        #         else:
        #             if nowC == ".":
        #                 result = result[:-1]
        #                 i+=2
        #             else:
        #                 i+=1
        # result = ["/"+val for val in result]
        # if len(result) == 0:
        #     return "/"
        # return "".join(result)

        plist = [p for p in path.split('/') if p]
        stack = []
        for p in plist:
            if p == '..':
                if stack:   stack.pop()
            elif p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)

if __name__ == '__main__':
    print(Solution().simplifyPath("/..."))