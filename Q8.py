class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0

        while not str[0].isnumeric():
            if (str[0] == '+' or str[0] == '-') and len(str)>1 and  str[1].isnumeric() or str[0].isnumeric():
                break
            elif not str[0] == ' ' and not str[0].isnumeric():
                return 0
            else:
                if len(str) < 2:
                    return 0
                str = str[1:]
        s = str[0]
        if len(str)>1:
            for a in str[1:]:
                if a.isnumeric():
                    s += a
                else:
                    break
        result = int(s)
        if result>0:
            return result if result<=2**31-1 else 2**31-1
        else:
            return result if result>=-2**31 else -2**31


if __name__ == '__main__':
    print(Solution().myAtoi("    +42afd"))




