class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def initNodeList(valList):
        if len(valList) == 0:
            return None
        head = ListNode(0)
        iterP = head
        for val in valList:
            p = ListNode(val)
            iterP.next = p
            iterP = iterP.next
        return head.next

    @staticmethod
    def linkListPrint(head):
        while head!=None:
            print(head.val)
            head = head.next