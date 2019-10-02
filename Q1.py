class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedNumId = sorted(range(len(nums)),key=lambda k:nums[k])
        tail = len(nums)
        head = 0
        while(tail>=head):
            if nums[sortedNumId[head]]+nums[sortedNumId[tail-1]]==target:
                break
            elif nums[sortedNumId[head]]+nums[sortedNumId[tail-1]]>target:
                tail-=1
            else:
                head+=1
        return [sortedNumId[head],sortedNumId[tail-1]]

    def twoSum(self,nums,target):
        hashmap = {}
        for index,num in enumerate(nums):
            anotherNum = target - num
            if anotherNum in hashmap:
                return [hashmap[anotherNum],index]
            hashmap[num] = index
        return None
if __name__ == '__main__':
    testList =[3,2,4]
    target = 6

    test = Solution()
    print(test.twoSum(testList,target))

