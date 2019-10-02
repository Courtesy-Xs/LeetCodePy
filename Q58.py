class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.strip())>0:
            loc=s.strip().rfind(' ')
            if loc == -1:
                return len(s.strip())
            else:
                return len(s.strip()[loc+1:])
        else:
            return 0