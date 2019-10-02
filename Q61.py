# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k==0:
            return head
        p,q = head,head
        count = 0
        bp = head
        outList = None
        while p:
            count+=1
            if count>k+1:
                bp = bp.next
            q = p
            p = p.next
        if count<=1:
            return head
        if count>k:
            outList = bp.next
            bp.next = None
            q.next = head
            return outList
        elif count==k:
            return head
        else:
            k = k%count
            if k==0:
                return head
            p = head
            for i in range(count-k-1):
                p = p.next
            outList = p.next
            p.next = None
            q.next = head
            return outList

if __name__ == '__main__':
    head = ListNode.initNodeList([1,2])
    resList =Solution().rotateRight(head,2)
    ListNode.linkListPrint(resList)





