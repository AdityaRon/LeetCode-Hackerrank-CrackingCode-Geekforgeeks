class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        self.head = head
        self.n = n
        current = head
        forward = head
        for i in range(n):
            current = current.next
        print(current)
        if not current:
            return head.next
        while current.next:
            current = current.next
            forward = forward.next
        forward.next = forward.next.next
        return head
