from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[]]
        dict_s = {}
        for s in strs:
            ls = sorted(list(s))
            ords = "".join(ls)
            if ords not in dict_s.keys():
                dict_s[ords] = [s]
            else:
                dict_s[ords].append(s)
        result = []
        for val in dict_s.values():
            result.append(val)
        return result


if __name__ == '__main__':
    print(Solution().groupAnagrams([]))





