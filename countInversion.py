class Solution:
    def Merge(self,A,L,leftCount,R,rightCount):
        k = 0
        count = 0;
        i,j = leftCount-1,rightCount-1
        while i >= 0 and j >= 0:
            if L[i] >3 * R[j]:
                count += (j+1);
                i-=1
            else:
                j-=1
        i,j =0,0
        while(i<leftCount and j<rightCount):
            if(L[i]<R[j]):
                A[k] = L[i]
                k+=1
                i+=1
            else:
                A[k] = R[j]
                k+=1
                j+=1
                # for m in range(i,len(L)):
                #     if L[m]>3*R[j-1]:
                #         count+=1
                #         print(str(L[m])+"  "+str(R[j-1]))
        while i < leftCount:
            A[k] = L[i]
            k+=1
            i+=1
        while j < rightCount:
            A[k] = R[j]
            k+=1
            j+=1
        return count;
    def MergeSort(self,A,n):
        if n<2:
            return 0
        mid = int(n/2)
        count = 0

        L,R=[],[]
        for i in range(mid):
            L.append(A[i])
        for i in range(mid,n):
            R.append(A[i])
        count+=self.MergeSort(L,mid);
        count+=self.MergeSort(R,n-mid);
        count+=self.Merge(A,L,mid,R,n-mid);
        return count;

if __name__ == '__main__':
    a = [13,8,5,3,2,1]
    n = len(a)
    print(Solution().MergeSort(a,n))