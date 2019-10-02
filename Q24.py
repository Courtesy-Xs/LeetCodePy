from ListNode import ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        l1 = ListNode(0)
        l1.next = head
        pf,p,q = l1,head,head.next
        while p and q:
            p.next = q.next
            q.next = p
            pf.next = q
            pf = p
            p = p.next
            if p is None:
                break
            q = p.next
        return l1.next

if __name__ == '__main__':
    head = ListNode.initNodeList([1,2])
    head = Solution().swapPairs(head)
    ListNode.linkListPrint(head)
