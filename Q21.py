
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head1 = ListNode(0)
        head1.next = l1
        l1f = head1
        head2 = ListNode(0)
        head2.next = l2
        l2f = head2
        while l1 and l2:
            if l1.val>l2.val:
                l1f.next = l2
                while l2 and l1.val>l2.val:
                    l2f = l2
                    l2 = l2.next
                l2f.next = l1
                l1.f = l2f
            else:
                l2f.next=l1
                while l1 and l1.val<=l2.val:
                    l1f = l1
                    l1 = l1.next
                l1f.next = l2
                l2.f = l1f
        return head1.next if head1.val<=head2.val else head2.next

if __name__ == '__main__':
    list1 =[-10,-9,-6,-4,1,9,9]
    list2 = [-5,-3,0,7,8,8]
    l1,l2 = ListNode(list1[0]),ListNode(list2[0])
    p,q = l1,l2
    for a in list1:
        p.next = ListNode(a)
        p = p.next
    for b in list2:
        q.next = ListNode(b)
        q = q.next
    head = Solution().mergeTwoLists(l1.next,l2.next)
    while head:
        print(head.val)
        head = head.next




