class Solution:
    def countAndSay(self, n: int) -> str:
        if n is 1:
            return "1"
        result = "1"
        for i in range(n-1):
            temp = []
            j = 0
            count = 1
            while j<len(result)-1:
                if result[j]==result[j+1]:
                    count+=1
                    j+=1
                else:
                    temp.append(str(count)+result[j])
                    count=1
                    j+=1
            temp.append(str(count)+result[j])
            result = "".join(temp)
        return result

if __name__ == '__main__':
    print(Solution().countAndSay(6))

