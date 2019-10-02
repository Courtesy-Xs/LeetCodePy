import sys
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)

        if(n>m):
            return Solution().findMedianSortedArrays(nums2,nums1)

        lMax1=lMax2=rMin1=rMin2=lo=0
        hi = 2*n

        while(hi>=lo):
            c1 = (hi+lo)/2
            c2 = m+n - c1

            lMax1 = nums1[(c1-1)/2] if (c1!=0) else -sys.maxsize
            rMin1 = nums1[c1/2] if (c1!=2*n) else sys.maxsize
            lMax2 = nums2[(c2-1)/2] if (c2!=0) else -sys.maxsize
            rMin2 = nums2[(c2/2)] if (c2!=2*m) else sys.maxsize

            if(lMax1>rMin2):
                hi = c1-1
            elif(lMax2>rMin1):
                lo = c1 +1
            else:
                break
        return (max(lMax1,lMax2)+min(rMin1,rMin2))/2.0


if __name__ == '__main__':
    print(sys.maxsize)

