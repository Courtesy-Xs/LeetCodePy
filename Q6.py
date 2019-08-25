class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s)
        if numRows ==1:
            return s

        goDown = False
        cur_row = 0
        rows = min(numRows,size)
        res = [""]*rows
        for i in range(size):
            res[cur_row]+=s[i]
            if cur_row==0 or cur_row==(rows-1):
                goDown = not goDown
            cur_row+= 1 if goDown else-1

        resString = ""
        for j in res:
            resString+=j
        return resString

if __name__ == '__main__':
    Solution().convert("PAYPALISHIRING",3)


