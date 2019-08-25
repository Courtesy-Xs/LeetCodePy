class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        size = len(s)
        isNegative = False
        if s[0] == "-":
            isNegative = True
            s = s[1:size-1]
            size-=1
        temp = ""
        half = int((size+1)/2)
        for i in range(half):
            temp = s[i]
            s[i] = s[2*half-i]
            s[2*half-i] = temp
        if s[0] == '0':
            if isNegative == True:
                s[0] = '-'
            else:
                s = s[1:size-1]
                size-=1
        return int(s)
