class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #
        iter = head = ListNode(0)
        p = l1
        q = l2
        carryBit = 0
        while(p or q):
            a = p.val if p else 0
            b = q.val if q else 0
            iter.val  = (a+b+carryBit)%10
            carryBit = (a+b+carryBit)/10
            flag = False
            if p:
                p = p.next
                flag = True
            if q:
                q = q.next
                flag = True
            if p or q:
                iter.next = ListNode(0)
                iter = iter.next
            elif carryBit:
                iter.next = ListNode(carryBit)
                iter = iter.next
            else:
                break
        return head
    def addTwoNumbelsBestAnswer(self,l1,l2):
        re = ListNode(0)
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1)
        return re.next

if __name__ == '__main__':
    l1 =ListNode(1)
    l2 =ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)

    solution = Solution()
    solution.addTwoNumbers(l1,l2)
