from ListNode import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return None
        p = head
        q = None
        count = 1
        while p.next!=None:
            count+=1
            p = p.next
        p = head
        if count is n:
            return p.next
        for i in range(count-n):
            q = p
            p = p.next
        q.next = p.next
        return head


if __name__ == '__main__':
    arr = [1,2]
    head = ListNode.initNodeList(arr)
    ListNode.linkListPrint(Solution().removeNthFromEnd(head,2))
