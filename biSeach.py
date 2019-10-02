class BiSearch:
    """
    "@Description:search by bisect
    "@param: nums:a sorted array in ascending
                  order  target:the value you want to search
    "@return: the index of target in nums, if not exists,then return -1
    "@throws:
    """
    def biSeach(self,nums,target):
        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

if __name__ == '__main__':
    nums = [1,2,2,2,2,2,3]
    print(BiSearch().biSeach(nums,2))